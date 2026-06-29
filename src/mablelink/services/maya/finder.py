from pathlib import Path


def find_maya_2024():
    possible_paths = [
        Path(r"C:\Program Files\Autodesk\Maya2024\bin\maya.exe"),
        Path(r"C:\Program Files\Autodesk\Maya 2024\bin\maya.exe"),
    ]

    for path in possible_paths:
        if path.exists():
            return path

    return None