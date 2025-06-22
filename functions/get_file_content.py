import os


def get_file_content(working_directory, file_path):
  abs_working_dir = os.path.abspath(working_directory)
  full_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

  # 1. Cek apakah path-nya keluar dari working dir
  if not full_file_path.startswith(abs_working_dir):
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  
  # 2. Cek apakah file ada dan valid
  if not os.path.isfile(full_file_path):
      return f'Error: File not found or is not a regular file: "{file_path}"'
  
  # 3. Baca isinya
  try:
      with open(full_file_path, "r", encoding="utf-8") as f:
          content = f.read(10001)
          if len(content) > 10000:
              return content[:10000] + "\n\n[truncated at 10000 characters]"
          return content
  except Exception as e:
      return f"Error: {e}"