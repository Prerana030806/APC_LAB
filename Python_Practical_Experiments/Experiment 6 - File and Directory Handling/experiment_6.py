from pathlib import Path

folder = Path("python_file_demo")
folder.mkdir(exist_ok=True)
file_path = folder / "sample.txt"

file_path.write_text("Python file handling demonstration.\nWelcome to Python.", encoding="utf-8")
print("File created:", file_path)
print("File content:")
print(file_path.read_text(encoding="utf-8"))

with file_path.open("a", encoding="utf-8") as file:
    file.write("\nNew line added to the file.")

print("Updated content:")
print(file_path.read_text(encoding="utf-8"))
print("Files in directory:", [item.name for item in folder.iterdir()])
print("File exists:", file_path.exists())
