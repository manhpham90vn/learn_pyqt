import shutil
import subprocess

# Remove build and dist directories
for folder in ["build", "dist"]:
    try:
        shutil.rmtree(folder)
        print(f"Deleted folder: {folder}")
    except FileNotFoundError:
        print(f"Folder {folder} not found.")
    except Exception as e:
        print(f"Error while deleting folder {folder}: {e}")
        exit(1)

# Run pyinstaller with poetry
try:
    subprocess.run(["poetry", "run", "pyinstaller", "app.spec"], check=True)
    print("PyInstaller command executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error while running the command: {e}")
