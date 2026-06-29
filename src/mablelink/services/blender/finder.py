from pathlib import Path


def find_blender():
    possible_paths = [
        Path(r"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe"),
        Path(r"C:\Program Files\Blender Foundation\Blender 3.1\blender.exe"),
    ]

    for path in possible_paths:
        if path.exists():
            return path

    return None