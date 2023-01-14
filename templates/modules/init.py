import json
import os
import shutil

from git import Repo


def main(base_dir, args):
    if args.get("-n"):
        with open(base_dir + "/env.json", encoding="utf-8") as file:
            js = json.loads(file.read())

        js["project_folder"] = os.getcwd()
        js["project_name"] = args["-n"]

        with open(base_dir + "/env.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(js, indent=4))
        print(f"creating project {args['-n']}...")
        os.mkdir(args["-n"])
        print(f"adding screens...")
        os.mkdir(f'{args["-n"]}/screens')
        print(f"adding templates...")
        os.mkdir(f'{args["-n"]}/templates')
        print(f"adding static...")
        os.mkdir(f'{args["-n"]}/static')
        print(f"adding HomeScreen...")
        shutil.copy(base_dir + "/templates/init/screens/HomeScreen.py", f'{args["-n"]}/screens')
        print(f"adding config...")
        shutil.copy(base_dir + "/templates/init/config.json", f'{args["-n"]}')
        print(f"adding main file...")
        shutil.copy(base_dir + "/templates/init/main.py", f'{args["-n"]}')
        print(f"adding index template...")
        shutil.copy(base_dir + "/templates/init/templates/index.html", f'{args["-n"]}/templates')
        print(f"adding run configurations...")
        with open(base_dir + "/env.json", encoding="utf-8") as file:
            with open(f"{args['-n']}/aem_run.json", "w") as file1:
                file1.write(file.read())
        print(f"cloning aengine_flask...")
        Repo.clone_from("https://github.com/aaalllexxx/aengine_flask", f"{args['-n']}/aengine_flask")

    else:
        print("Следует использовать флаг '-n' для указания имени проекта")
