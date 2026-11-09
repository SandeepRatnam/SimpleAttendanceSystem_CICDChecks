from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

# Get the project directory
project_folder = Path(__file__).parent

# Create a dist folder
dist_folder = project_folder / "dist"
dist_folder.mkdir(exist_ok=True)

# Define the ZIP file location
zip_path = dist_folder / "attendance-app.zip"

# Files to include in the ZIP package
files_to_package = [
    "attendance.py",
    "README.md"
]

# Create the ZIP package
with ZipFile(zip_path, "w", ZIP_DEFLATED) as zip_file:

    for filename in files_to_package:

        file_path = project_folder / filename

        zip_file.write(file_path, arcname=filename)

print("Build completed successfully!")
print("Artifact created:", zip_path)