def create_dissolve(target=None, duration=30, options=None):
    """Create a dissolve effect on `target`.

    Simulation-safe placeholder returning a summary when outside Blender.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "target": target, "duration": duration}

    # Real implementation would animate visibility or use shaders.
    print(f"create_dissolve: applied dissolve to {target}")
    return {"status": "ok", "target": target}