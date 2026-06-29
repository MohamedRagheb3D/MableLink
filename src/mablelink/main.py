print("MAIN FILE IS RUNNING")
from mablelink.services.maya.status import is_maya_running
from mablelink.application.engine import Engine
from mablelink.version import APP_NAME, VERSION
from mablelink.services.maya.finder import find_maya_2024
from mablelink.services.maya.launcher import launch_maya


def main():
    print("=" * 50)
    print(APP_NAME)
    print(f"Version {VERSION}")
    print("=" * 50)

    engine = Engine()
    engine.start()

maya = find_maya_2024()

if maya:

    print(f"\nMaya Found:\n{maya}")

    if is_maya_running():
        print("\nMaya is already running.")
    else:
        print("\nLaunching Maya...")
        launch_maya()

else:
    print("\nMaya 2024 Not Found.")