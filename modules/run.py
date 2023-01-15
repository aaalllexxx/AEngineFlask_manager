import json
import os
import platform
import subprocess


def main(base_dir, _):
    try:
        if os.path.exists("aem_run.json"):
            with open("aem_run.json") as file:
                js = json.loads(file.read())
                print(f"Found run configuration.\nRunning {js['project_name']} application.")

        else:
            with open(base_dir + "/env.json") as file:
                js = json.loads(file.read())
                print(f"Didn't find run configuration.\nRunning {js['project_name']} application.")
        project_folder = js["project_folder"]
        print(project_folder)
        project_name = js["project_name"]
        print(project_name)
        if platform.system().lower() == "windows":
            command = f"python \"{os.path.join(project_folder, project_name)}\\main.py\""
            try:
                subprocess.call(command)
            except OSError as e:
                print(e)
    except KeyboardInterrupt:
        print("bye bye!")
        raise SystemExit(0)
