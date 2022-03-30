# type: ignore

import os

import fire


class Cli:
    def build_and_release(self):
        result = os.system("sudo rm -rf dist/* || true")
        result = os.system("python3 -m build")

        if result != 0:
            raise Exception("Build failed")
        os.system("python3 -m twine upload dist/* ")


fire.Fire(Cli)
