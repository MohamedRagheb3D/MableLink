from mablelink.services.maya.launcher import launch_maya
from mablelink.services.maya.status import is_maya_running

from mablelink.services.blender.launcher import launch_blender
from mablelink.services.blender.status import is_blender_running


def send_to_blender():

    print("========== SEND TO BLENDER ==========")

    if is_maya_running():
        print("Maya is already running.")
    else:
        print("Launching Maya...")
        launch_maya()

    if is_blender_running():
        print("Blender is already running.")
    else:
        print("Launching Blender...")
        launch_blender()

    print("Done.")