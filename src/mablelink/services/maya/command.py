from pathlib import Path


def create_test_script():
    script = Path.home() / "mablelink_test.py"

    script.write_text(
        """
import maya.cmds as cmds

cmds.confirmDialog(
    title="MableLink",
    message="Hello from MableLink!"
)
""",
        encoding="utf-8"
    )

    return script