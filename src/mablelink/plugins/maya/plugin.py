import maya.cmds as cmds


def initializePlugin(plugin):
    cmds.confirmDialog(
        title="MableLink",
        message="Hello from MableLink!"
    )


def uninitializePlugin(plugin):
    print("MableLink Plugin Unloaded")