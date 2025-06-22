import os


def write_file(working_directory, file_path, content):
  abs_working_dir = os.path.abspath(working_directory)
  full_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

  # 1. Cek apakah path-nya keluar dari working dir
  if not full_file_path.startswith(abs_working_dir):
      return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

  try:
        # 2. Buat folder kalau belum ada
        os.makedirs(os.path.dirname(full_file_path), exist_ok=True)

        # 3. Tulis file
        with open(full_file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
        return f"Error: {e}"