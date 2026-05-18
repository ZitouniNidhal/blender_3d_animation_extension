from . import resolve_target


def create_explosion(origin=None, strength=1.0, options=None):
    """Create an explosion effect at `origin`.

    This places a point-force field in the scene and animates its strength.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "origin": origin, "strength": strength}

    scene = bpy.context.scene
    if origin is None:
        coords = getattr(scene.cursor, 'location', (0.0, 0.0, 0.0))
    elif isinstance(origin, (list, tuple)) and len(origin) >= 3:
        coords = (origin[0], origin[1], origin[2])
    else:
        obj, _ = resolve_target(origin)
        coords = obj.location.copy() if obj is not None else getattr(scene.cursor, 'location', (0.0, 0.0, 0.0))

    empty = bpy.data.objects.new('Anim3D_Explosion', None)
    empty.location = coords
    bpy.context.collection.objects.link(empty)

    field = empty.field
    field.type = 'FORCE'
    field.shape = 'POINT'
    field.strength = float(strength) * 300.0
    field.distance_max = 5.0 + float(strength) * 5.0
    field.flow = 1.0
    field.use_gravity = False
    field.falloff_power = 2.0

    start_frame = scene.frame_start
    empty.keyframe_insert('location', frame=start_frame)
    field.keyframe_insert('strength', frame=start_frame)

    field.strength = 0.0
    field.keyframe_insert('strength', frame=start_frame + 15)

    return {"status": "ok", "origin": coords, "strength": strength, "object": empty.name}