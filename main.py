import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
user_prompt = sys.argv[1]
args = sys.argv[1:]

messages = [
	types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
hasVerbose = "--verbose" in args

response = client.models.generate_content(
	model='gemini-2.0-flash-001',
	contents=messages,
)

response_usage = response.usage_metadata

if hasVerbose:
	print(f"User prompt: {user_prompt}")
	print(f"Prompt tokens: {response_usage.prompt_token_count}")
	print(f"Response tokens: {response_usage.candidates_token_count}")

