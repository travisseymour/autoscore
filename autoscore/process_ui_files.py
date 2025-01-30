from pathlib import Path
from typing import List

from plumbum.colors import cyan, yellow, red, green, bold
from plumbum import local

"""
This converts .ui files to .py files for PyQt6, but to keep GIT history accurate, 
I only want to process ui files that actually changed.
"""


ui_files: List[Path] = list(Path().glob("*.ui"))

if not ui_files:
    print("No ui files found...nothing to do." | yellow & bold)

print(f"Checking {len(ui_files)} ui files for potential changes..." | yellow & bold)

found_anything = False

for ui in ui_files:
    py = ui.with_suffix(".py")
    if not py.is_file() or ui.stat().st_mtime > py.stat().st_mtime:
        found_anything = True
        print(f"Converting {ui.name} to {py.name}" | cyan)
        try:
            local["pyside6-uic"]([str(ui.resolve()), "-o", str(py.resolve())])
            print("\tSuccess!" | green)
        except Exception as e:
            print(f"\tERROR: {e}" | red & bold)

if not found_anything:
    print("All files up to date. Nothing done." | yellow & bold)

print("Finished." | yellow & bold)
