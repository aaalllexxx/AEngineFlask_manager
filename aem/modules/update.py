import getpass
import os
import subprocess
import sys
from shutil import *


def copy_and_overwrite(src, dst, symlinks=False, ignore=None):
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    if not os.path.isdir(dst):  # This one line does the trick
        os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks, ignore)
            else:
                # Will raise a SpecialFileError for unsupported file types
                copy2(srcname, dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
        except EnvironmentError as why:
            errors.append((srcname, dstname, str(why)))
    try:
        copystat(src, dst)
    except OSError as why:
        if WindowsError is not None and isinstance(why, WindowsError):
            # Copying file access times may fail on Windows
            pass
        else:
            errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)


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
        copy_and_overwrite(f"{os.getcwd()}", f"C:/Users/{getpass.getuser()}")
        print("full update done.")
