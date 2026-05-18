from . import resolve_target


def create_dissolve(target=None, duration=30, options=None):
    """Create a dissolve effect on `target`.

    This animates the object's material transparency over time.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "target": target, "duration": duration}

    obj, _ = resolve_target(target)
    if obj is None:
        bpy.ops.mesh.primitive_cube_add(size=2.0)
        obj = bpy.context.active_object

    if not obj.data.materials:
        mat = bpy.data.materials.new('Anim3D_DissolveMaterial')
        obj.data.materials.append(mat)
    else:
        mat = obj.active_material or obj.data.materials[0]
        if mat is None:
            mat = bpy.data.materials.new('Anim3D_DissolveMaterial')
            obj.data.materials[0] = mat

    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    output_node = nodes.get('Material Output') or nodes.new('ShaderNodeOutputMaterial')
    principled = next((node for node in nodes if node.type == 'BSDF_PRINCIPLED'), None)
    if principled is None:
        principled = nodes.new('ShaderNodeBsdfPrincipled')
        principled.location = (-200, 0)

    transparent = nodes.new('ShaderNodeBsdfTransparent')
    transparent.location = (-200, -200)

    mix_shader = nodes.new('ShaderNodeMixShader')
    mix_shader.location = (0, 0)

    dissolve_value = nodes.new('ShaderNodeValue')
    dissolve_value.name = 'Dissolve_Value'
    dissolve_value.location = (-400, 0)

    links.new(dissolve_value.outputs[0], mix_shader.inputs[0])
    links.new(principled.outputs[0], mix_shader.inputs[1])
    links.new(transparent.outputs[0], mix_shader.inputs[2])
    links.new(mix_shader.outputs[0], output_node.inputs['Surface'])

    mat.blend_method = 'BLEND'
    mat.shadow_method = 'NONE'

    scene = bpy.context.scene
    start_frame = scene.frame_start
    end_frame = start_frame + int(duration)

    dissolve_value.outputs[0].default_value = 1.0
    dissolve_value.keyframe_insert('default_value', frame=start_frame)

    dissolve_value.outputs[0].default_value = 0.0
    dissolve_value.keyframe_insert('default_value', frame=end_frame)

    return {"status": "ok", "target": obj.name, "duration": duration}