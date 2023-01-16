import os

if not os.path.isdir("venv"):
    os.system("python -m venv venv")
    os.system("venv/Scripts/activate")
    os.system("pip install -r ../req.txt")
print("ready")
