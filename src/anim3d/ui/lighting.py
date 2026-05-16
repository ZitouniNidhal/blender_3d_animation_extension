try:
    import bpy
except Exception:
    bpy = None


def setup_three_point_lighting(preset="STUDIO"):
    lights = ["key", "fill", "rim"]
    if bpy is None:
        return {"status": "simulated", "lights_created": lights}

    scene = bpy.context.scene
    if scene is None:
        return {"status": "error", "message": "No active scene."}

    world = scene.world
    if world is None:
        world = bpy.data.worlds.new("Anim3D_World")
        scene.world = world

    settings = {
        "STUDIO": {"key_energy": 1200, "fill_energy": 250, "rim_energy": 180},
        "OUTDOOR": {"key_energy": 3000, "fill_energy": 1000, "rim_energy": 500},
        "DRAMATIC": {"key_energy": 1800, "fill_energy": 400, "rim_energy": 250},
        "SOFT": {"key_energy": 600, "fill_energy": 250, "rim_energy": 180},
        "NEON": {"key_energy": 1000, "fill_energy": 300, "rim_energy": 600},
    }
    values = settings.get(preset.upper(), settings["STUDIO"])

    created = []
    origin = bpy.context.scene.cursor.location.copy()

    for name, energy, location in [
        ("Key", values["key_energy"], (2.0, -3.0, 4.5)),
        ("Fill", values["fill_energy"], (-2.0, -2.5, 3.0)),
        ("Rim", values["rim_energy"], (0.0, 3.0, 4.5)),
    ]:
        light_data = bpy.data.lights.new(f"Anim3D_{name}", type="AREA")
        light_data.energy = energy
        light_obj = bpy.data.objects.new(f"Anim3D_{name}", light_data)
        light_obj.location = location
        scene.collection.objects.link(light_obj)
        created.append(light_obj.name)

    return {"status": "ok", "lights_created": created}


def setup_dynamic_lighting(intensity_curve=None, frame_start=1, frame_end=250):
    if bpy is None:
        return {"status": "simulated", "keyframes_set": len(intensity_curve) if intensity_curve else 0}

    if intensity_curve is None:
        intensity_curve = [(1, 1.0), (125, 2.0), (250, 1.0)]

    scene = bpy.context.scene
    light_data = bpy.data.lights.new("Anim3D_Dynamic", type="SUN")
    light_obj = bpy.data.objects.new("Anim3D_Dynamic", light_data)
    light_obj.rotation_euler = (1.2, 0.0, 0.8)
    scene.collection.objects.link(light_obj)

    for frame, value in intensity_curve:
        light_data.energy = value * 1000
        light_data.keyframe_insert(data_path="energy", frame=frame)

    return {"status": "ok", "keyframes_set": len(intensity_curve)}


def setup_ambient_lighting(energy=0.5):
    if bpy is None:
        return {"status": "simulated", "energy": energy}

    scene = bpy.context.scene
    world = scene.world
    if world is None:
        world = bpy.data.worlds.new("Anim3D_World")
        scene.world = world

    if world.use_nodes:
        if not world.node_tree:
            world.use_nodes = True
        bg = world.node_tree.nodes.get("Background")
        if bg is None:
            bg = world.node_tree.nodes.new(type="ShaderNodeBackground")
            world.node_tree.nodes.new(type="ShaderNodeOutputWorld")
        bg.inputs[1].default_value = energy
    else:
        world.light_settings.use_ambient_occlusion = True
        world.light_settings.ao_factor = energy

    return {"status": "ok", "energy": energy}
