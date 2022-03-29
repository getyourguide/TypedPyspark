from __future__ import annotations

from typing import Callable

from mypy.plugin import Plugin


class CustomPlugin(Plugin):
    def main(self, func):
        return func.api.fail("Typed-Pyspark failed to load as plugin")

    def get_function_hook(self, name):
        if name == "DF":
            return self.main
        else:
            return None


def plugin(version):
    return CustomPlugin
