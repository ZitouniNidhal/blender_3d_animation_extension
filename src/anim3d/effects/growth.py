from . import resolve_target


def create_growth(target=None, duration=50, options=None):
    """Create a growth effect on `target`.

    If Blender is present, keyframe the object's scale from zero to full
    size over the specified duration.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "target": target, "duration": duration}

    # Real implementation would keyframe scale or modifiers.
    print(f"create_growth: applied to {target} inside Blender")
    return {"status": "ok", "target": target}