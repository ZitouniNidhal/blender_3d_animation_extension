bl_info = {
    "name": "Anim3D",
    "author": "ZitouniNidhal",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Tool Shelf",
    "description": "Procedural 3D animation generator",
    "category": "Animation",
}

from . import addon as addon_module


def _register_bpy():
    from .operators import register as register_operators
    from .ui.panels_main import register as register_main_ui
    from .ui.panels_lighting import register as register_lighting_ui

    register_operators()
    register_main_ui()
    register_lighting_ui()


def _unregister_bpy():
    from .operators import unregister as unregister_operators
    from .ui.panels_main import unregister as unregister_main_ui
    from .ui.panels_lighting import unregister as unregister_lighting_ui

    unregister_lighting_ui()
    unregister_main_ui()
    unregister_operators()


def register():
    try:
        import bpy  # noqa: F401
        addon_module.register()
        _register_bpy()
        print("Anim3D registered inside Blender")
    except Exception:
        print("Anim3D register simulated (no Blender)")


def unregister():
    try:
        import bpy  # noqa: F401
        addon_module.unregister()
        _unregister_bpy()
        print("Anim3D unregistered inside Blender")
    except Exception:
        print("Anim3D unregister simulated (no Blender)")