import subprocess

from mablelink.services.blender.finder import find_blender


def launch_blender():
    blender = find_blender()

    if blender is None:
        return False

    subprocess.Popen([str(blender)])

    return True