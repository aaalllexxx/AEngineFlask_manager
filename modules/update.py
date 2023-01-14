import subprocess

from git.repo import Repo


def main(base_dir, args):
    url = "https://github.com/aaalllexxx/AEngineFlask_manager"
    print(f"cloning from {url}...")
    Repo.clone_from(url, base_dir)
    print("configuring...")
    subprocess.call(base_dir + "/init.bat")
