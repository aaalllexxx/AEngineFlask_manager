import getpass
import os


def main(*_):
    if not os.path.isdir("venv"):
        os.system("python -m venv venv")
    os.system("cd venv/Scripts/")
    os.system(f"pip install -r C:/Users/{getpass.getuser()}/aem/req.txt")
    print("ready")
