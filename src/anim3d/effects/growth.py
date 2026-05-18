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

    obj, _ = resolve_target(target)
    scene = bpy.context.scene
    if obj is None:
        mesh = bpy.data.meshes.new('Anim3D_GrowthMesh')
        obj = bpy.data.objects.new('Anim3D_Growth', mesh)
        bpy.context.collection.objects.link(obj)

    start_frame = scene.frame_start
    end_frame = start_frame + int(duration)

    obj.scale = (0.0, 0.0, 0.0)
    obj.keyframe_insert('scale', frame=start_frame)

    obj.scale = (1.0, 1.0, 1.0)
    obj.keyframe_insert('scale', frame=end_frame)

    return {"status": "ok", "target": obj.name, "duration": duration}