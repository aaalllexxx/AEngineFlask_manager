import getpass
import os
import subprocess


def main(base_dir, args):
    os.chdir(f"C:/Users/{getpass.getuser()}/aem")
    subprocess.call("git pull")
