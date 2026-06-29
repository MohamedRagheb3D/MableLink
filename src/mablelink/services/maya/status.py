import psutil


def is_maya_running():
    for process in psutil.process_iter(["name"]):
        try:
            if process.info["name"] and process.info["name"].lower() == "maya.exe":
                return True
        except Exception:
            pass

    return False