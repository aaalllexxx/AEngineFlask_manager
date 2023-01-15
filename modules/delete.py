import json
import os
import platform


def main(*_):
    try:
        if os.path.exists("aem_run.json"):
            with open("aem_run.json") as file:
                js = json.loads(file.read())
                print(f"Found configuration.\nDeleting {js['project_name']} application.")

        else:
            print(f"Didn't find configurations.")
            raise SystemExit(0)
        project_folder = js["project_folder"]
        project_name = js["project_name"]
        if platform.system().lower() == "windows":
            command = f"del /S \"{os.path.join(project_folder, project_name)}\""
            try:
                os.system(command)
            except OSError as e:
                print(e)
    except KeyboardInterrupt:
        print("bye bye!")
        raise SystemExit(0)
