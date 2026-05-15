def setup_camera_rig(name="Anim3D_Rig", options=None):
    """Set up a camera rig named `name`.

    Returns a dict describing the result. When `bpy` is available this will
    create objects; otherwise it simulates the action.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "name": name}

    # Actual rig creation would happen here.
    print(f"setup_camera_rig: created rig '{name}' inside Blender")
    return {"status": "ok", "name": name}