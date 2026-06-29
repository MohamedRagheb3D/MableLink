import subprocess

from mablelink.services.maya.finder import find_maya_2024


def launch_maya():
    maya = find_maya_2024()

    if maya is None:
        return False

    subprocess.Popen([str(maya)])

    return True