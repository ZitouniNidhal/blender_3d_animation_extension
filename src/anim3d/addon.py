def register():
    try:
        import bpy
        print("Anim3D addon: registering classes")
    except Exception:
        print("Anim3D addon: register simulated (no Blender)")


def unregister():
    try:
        import bpy
        print("Anim3D addon: unregistering classes")
    except Exception:
        print("Anim3D addon: unregister simulated (no Blender)")