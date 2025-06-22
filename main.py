import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
user_prompt = sys.argv[1]
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

args = sys.argv[1:]
hasVerbose = "--verbose" in args

messages = [
	types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

schema_get_files_info = types.FunctionDeclaration(
	name="get_files_info",
	description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
	parameters=types.Schema(
		type=types.Type.OBJECT,
		properties={
			"directory": types.Schema(
				type=types.Type.STRING,
				description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
			),
		},
	),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

response = client.models.generate_content(
	model='gemini-2.0-flash-001',
	contents=messages,
	config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
)

response_usage = response.usage_metadata
function_call_part = response.function_calls

print(response.text)

if function_call_part:
	print(f"Calling function: {function_call_part[0].name}({function_call_part[0].args})")

if hasVerbose:
	print(f"User prompt: {user_prompt}")
	print(f"Prompt tokens: {response_usage.prompt_token_count}")
	print(f"Response tokens: {response_usage.candidates_token_count}")

