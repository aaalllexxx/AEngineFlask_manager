import json
import os
import platform
import subprocess


def main(base_dir, _):
    try:
        if os.path.exists("aem_run.json"):
            with open("aem_run.json") as file:
                js = json.loads(file.read())
                print(f"Конфигурации найдены.\nЗапуск приложения '{js['project_name']}'.")

        else:
            with open(base_dir + "/env.json") as file:
                js = json.loads(file.read())
                print(f"Конфигурации не найдены.\nЗапуск приложения '{js['project_name']}'.")
        project_folder = js["project_folder"]
        project_name = js["project_name"]
        if platform.system().lower() == "windows":
            command = f"python \"{os.path.join(project_folder, project_name)}\\main.py\""
            try:
                subprocess.call(command)
            except OSError as e:
                print(e)
    except KeyboardInterrupt:
        print("bye bye!")
        raise SystemExit(0)
