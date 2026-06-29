print("MAIN FILE IS RUNNING")

from mablelink.application.engine import Engine
from mablelink.version import APP_NAME
from mablelink.version import VERSION


def main():

    print("=" * 50)
    print(APP_NAME)
    print(f"Version {VERSION}")
    print("=" * 50)

    engine = Engine()

    engine.start()


if __name__ == "__main__":
    main()

