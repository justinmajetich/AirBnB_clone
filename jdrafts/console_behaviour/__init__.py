#!/usr/bin/python3

from pathlib import Path

this_file = Path(__file__).absolute()
this_folder = this_file.parent

__all__ = [
    x.stem for x in this_folder.parent.rglob("*.py")
        if (
            (x.parent.stem == this_folder.stem)
        ) and not x.stem.startswith("__")
]
del Path 