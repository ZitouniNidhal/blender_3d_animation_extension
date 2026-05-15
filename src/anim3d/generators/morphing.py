def generate_morphing(targets=None, duration=100, options=None):
    """Generate morphing animation between `targets`.

    This is a simulation-safe placeholder. When `bpy` is present it will
    attempt to operate on mesh shape keys; otherwise it returns a description
    of the intended action.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "targets": targets, "duration": duration}

    # Real implementation would manipulate shape keys / keyframes here.
    print("generate_morphing: running inside Blender")
    return {"status": "ok", "targets": targets, "duration": duration}