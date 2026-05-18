from . import resolve_target


def create_fracture(target=None, pieces=10, options=None):
    """Create a fracture effect on `target` dividing it into `pieces`.

    This duplicates the mesh as shards and offsets them slightly for a
    fractured look.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "target": target, "pieces": pieces}

    try:
        import random
        from mathutils import Vector
    except Exception:
        random = None
        Vector = None

    if bpy is None or random is None or Vector is None:
        return {"status": "simulated", "target": target, "pieces": pieces}

    source, _ = resolve_target(target)
    if source is None or source.type != 'MESH':
        mesh = bpy.data.meshes.new('Anim3D_FractureMesh')
        source = bpy.data.objects.new('Anim3D_FractureSource', mesh)
        bpy.context.collection.objects.link(source)

    shards = []
    base_location = source.location.copy()
    for index in range(max(1, int(pieces))):
        shard = source.copy()
        shard.data = source.data.copy()
        shard.name = f"{source.name}_shard_{index + 1}"
        shard.location = base_location.copy()
        bpy.context.collection.objects.link(shard)

        displacement = Vector((
            random.uniform(-0.25, 0.25),
            random.uniform(-0.25, 0.25),
            random.uniform(-0.25, 0.25),
        ))
        shard.location += displacement
        shards.append(shard.name)

    source.hide_viewport = True
    source.hide_render = True

    return {"status": "ok", "target": source.name, "pieces": len(shards), "shards": shards}