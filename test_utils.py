import distutils.sysconfig as sysconfig
import os
from typing import Set


def _get_std_modules() -> Set[str]:
    """
    Returns a set with all Python std modules

    Source: https://stackoverflow.com/a/6464112

    Note:
    There's a cooler way in Python 3.10 (https://stackoverflow.com/a/21659703)
    but I'm aware that not all Pythoners use 3.10 currently.

    Returns:
        Set[str]: A set with all current Python std modules
    """
    modules_set = set()
    std_lib = sysconfig.get_python_lib(standard_lib=True)

    for top, _, files in os.walk(std_lib):
        for nm in files:
            if nm != "__init__.py" and nm[-3:] == ".py":
                modules_set.add(
                    os.path.join(top, nm)[len(std_lib) + 1 : -3].replace("\\", ".")
                )

    return modules_set


def is_module_in_stl(module_name: str) -> bool:
    return module_name in _get_std_modules()
