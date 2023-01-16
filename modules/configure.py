import os


def main(base_dir, args):
    if not os.path.isdir("venv"):
        os.system("python -m venv venv")
        os.system("venv/Scripts/activate")
        os.system("pip install -r ../req.txt")
    print("ready")
