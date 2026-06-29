print("MAIN FILE IS RUNNING")

from mablelink.application.engine import Engine
from mablelink.version import APP_NAME, VERSION
from mablelink.services.maya.finder import find_maya_2024


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
    else:
        print("\nMaya 2024 Not Found.")


if __name__ == "__main__":
    main()