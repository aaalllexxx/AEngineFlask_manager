import getpass
import os
import subprocess


def main(*_):
    base = f"C:/Users/{getpass.getuser()}/aem"
    if not os.path.exists(os.path.join(base, "temp")):
        os.mkdir(os.path.join(base, "temp"))
    os.chdir(os.path.join(base, "temp"))
    temp = os.path.join(base, "temp")
    aem = os.path.join(temp, "AEngineFlask_manager")
    if not os.path.exists(aem):
        subprocess.call("git clone https://github.com/aaalllexxx/AEngineFlask_manager/")
    else:
        os.chdir(aem)
        subprocess.call("git pull")
    os.system(os.path.join(aem, "update.bat"))
