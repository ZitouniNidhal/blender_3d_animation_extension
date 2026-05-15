bl_info = {
    "name": "Anim3D",
    "author": "ZitouniNidhal",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Tool Shelf",
    "description": "Procedural 3D animation generator",
    "category": "Animation",
}

def register():
    try:
        import bpy
        print("Anim3D: register called inside Blender")
    except Exception:
        print("Anim3D: register simulated (not running inside Blender)")

def unregister():
    try:
        import bpy
        print("Anim3D: unregister called inside Blender")
    except Exception:
        print("Anim3D: unregister simulated (not running inside Blender)")