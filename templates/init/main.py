import os
from aengine_flask.app import App

base_dir = os.path.dirname(os.path.realpath(__file__))


class MyApp(App):
    def __init__(self):
        self.load_config(base_dir + "/config.json")


if __name__ == "__main__":
    app = MyApp()
    app.set_root_folder(base_dir)
    app.run("127.0.0.1", 80, debug=True)
