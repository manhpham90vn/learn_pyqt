import shutil
import subprocess

# Remove build and dist directories
for folder in ["build", "dist"]:
    try:
        shutil.rmtree(folder)
        print(f"Deleted folder: {folder}")
    except FileNotFoundError:
        print(f"Folder {folder} does not exist, skipping.")

# Run pyinstaller with poetry
try:
    subprocess.run(["poetry", "run", "pyinstaller", "app.spec"], check=True)
    print("PyInstaller command executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error while running the command: {e}")
