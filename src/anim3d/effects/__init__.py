"""Anim3D effects package."""

from typing import Optional, Tuple


def resolve_target(target=None):
    """Resolve a Blender object by name or instance.

    Returns a tuple of (object, resolved_name). If no object is found, returns
    (None, None).
    """
    try:
        import bpy
    except Exception:
        return None, None

    if target is None:
        return bpy.context.active_object, getattr(bpy.context.active_object, 'name', None)

    if isinstance(target, str):
        obj = bpy.data.objects.get(target)
        return obj, target if obj is not None else None

    if hasattr(target, 'name'):
        return target, target.name

    return None, None
