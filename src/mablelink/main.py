print("MAIN FILE IS RUNNING")

from mablelink.services.maya.status import is_maya_running
from mablelink.application.engine import Engine
from mablelink.version import APP_NAME, VERSION
from mablelink.services.maya.finder import find_maya_2024
from mablelink.services.maya.launcher import launch_maya
from mablelink.application.send_to_blender import send_to_blender


def main():

    print("=" * 50)
    print(APP_NAME)
    print(f"Version {VERSION}")
    print("=" * 50)

    engine = Engine()
    engine.start()

    send_to_blender()


if __name__ == "__main__":
    main()