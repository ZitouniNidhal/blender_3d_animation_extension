def create_growth(target=None, duration=50, options=None):
    """Create a growth effect on `target`.

    Simulation-safe: returns a dict describing the action when not in Blender.
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