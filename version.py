import re
import os
import sys

__major = 0
__minor = 0
__patch = 5
__build = 1

"""
    This file contains the version of the project (above) and is easily updatable manually of programmatically. 
    The increase is always of 1.

    A version update means that te file rewrite itself and will expose the new version at the next reload of the module

    numbers are  0="major", 1="minor", 2="patch", 3="build". 


    @usage : You can import the library in your code with `import 'version'` or you can call it with python like so : `python version.py <version_lvl>` 
"""


def increment_version(level=3):
    """
    The increase is always of 1.
    A version update means that te file rewrite itself and will expose the new version at the next reload of the module

    @param level: which level to increment : 0="major", 1="minor", 2="patch", 3="build"
    @return: None the file has rewritten itself
    """
    if level > 4 or level is None:
        level = 3

    vtypes = ["major", "minor", "patch", "build"]
    vtype_to_incr = vtypes[level]
    vtypes_to_reset = vtypes[-(3-level):] if -(3-level) != 0 else []
    newlines = []
    with open(os.path.abspath(__file__), 'r') as file:
        lines = file.readlines()
        for line in lines:
            # match the line to update
            if re.match(r"__\w{5,7}\s?=\s?\d+", line) and vtype_to_incr in line:
                line = f"__{vtype_to_incr} = {(int(line.split('=')[1]) + 1)}\n"
            for vtype_to_reset in vtypes_to_reset:
                if re.match(r"__\w{5,7}\s?=\s?\d+", line) and vtype_to_reset in line:
                    line = f"__{vtype_to_reset} = 0\n"
            newlines.append(line)

    with open(os.path.abspath(__file__), 'w') as file:
        file.writelines(newlines)


__version__ = ".".join(
    map(lambda i: str(i), [__major, __minor, __patch, __build]))


def get_version() -> str:
    """
        return full version
    """
    return __version__


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You need to define the level of version to update. Usage python version.py <version_lvl>")
        exit()

    ver_lvl = int(sys.argv[1])
    increment_version(ver_lvl)
    exit(0)
