import psutil


def is_blender_running():

    for process in psutil.process_iter(["name"]):

        try:
            if process.info["name"] and process.info["name"].lower() == "blender.exe":
                return True
        except Exception:
            pass

    return False