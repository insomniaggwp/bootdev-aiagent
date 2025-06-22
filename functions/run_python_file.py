import os
import subprocess


def run_python_file(working_directory, file_path):
  abs_working_dir = os.path.abspath(working_directory)
  full_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

  if not full_file_path.startswith(abs_working_dir):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  
  if not os.path.isfile(full_file_path):
    return f'Error: File "{file_path}" not found.'
  
  if not file_path.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file.'

  try:
    result = subprocess.run(
        ["python3", full_file_path],
        capture_output=True,
        timeout=30,
        text=True 
    )
    print("subprocess", result)

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    
    output = result.stdout.strip()
    error = result.stderr.strip()

    if result.returncode != 0:
        return f"Process exited with code {result.returncode}.\n{error or 'No output produced.'}"

    if not output:
        return "No output produced."

    return output

  except subprocess.TimeoutExpired:
      return "Error: Execution timed out."
  except Exception as e:
      return f"Error: executing Python file: {e}"