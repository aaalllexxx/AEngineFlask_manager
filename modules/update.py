import getpass
import os
import shutil
import subprocess
import sys


def copy_and_overwrite(src, dst):
    for file in os.listdir(src):
        name = os.path.join(src, file)
        if os.path.isfile(name):
            try:
                shutil.copy(name, dst)
                print(f"succesfully copied {file}")
            except OSError as e:
                print(e)
        else:
            try:
                shutil.copytree(name, dst)
                print(f"succesfully copied {file}")
            except OSError as e:
                print(e)


def main(*_):
    if not ("--full" in sys.argv):
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
        print("update done.")

    else:
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
        print(os.getcwd())
        os.system(os.path.join(aem, "update.bat"))
        copy_and_overwrite(f"{os.getcwd()}", f"C:/Users/{getpass.getuser()}/aem")
        print("full update done.")
