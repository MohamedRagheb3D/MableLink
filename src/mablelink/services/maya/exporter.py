from pathlib import Path


def export_usd_path():
    return Path.home() / "Desktop" / "mablelink_scene.usda"


def export_scene():
    return export_usd_path()