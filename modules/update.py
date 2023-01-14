import os
import subprocess


def main(base_dir, args):
    os.system(os.path.join(base_dir, "to_user_folder.bat"))
    subprocess.call("git pull")
