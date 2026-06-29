import subprocess

from mablelink.services.maya.finder import find_maya_2024
from mablelink.services.maya.command import create_test_script


def launch_maya():
    maya = find_maya_2024()

    if maya is None:
        return False

    script = create_test_script()

    subprocess.Popen([
        str(maya),
        "-command",
        f'python("exec(open(r\'{script}\').read())")'
    ])

    return True