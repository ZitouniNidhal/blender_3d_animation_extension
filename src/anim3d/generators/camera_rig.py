def setup_camera_rig(name="Anim3D_Rig", location=(0.0, -6.0, 4.0), target_location=(0.0, 0.0, 1.0), options=None):
    """Set up a camera rig named `name` with tracking constraint.

    Args:
        name: Name prefix for the rig objects
        location: Camera position (x, y, z)
        target_location: Target position for track-to constraint (x, y, z)
        options: Optional dict with additional parameters

    Returns dict with status, camera name, and target name (or simulated response).
    """
    try:
        import bpy
        from mathutils import Vector
    except Exception:
        return {"status": "simulated", "name": name}

    scene = bpy.context.scene

    # Create camera
    camera_data = bpy.data.cameras.new(f"{name}_Camera")
    camera_object = bpy.data.objects.new(f"{name}_Camera", camera_data)
    scene.collection.objects.link(camera_object)
    camera_object.location = Vector(location)
    camera_object.rotation_euler = (1.2, 0.0, 0.0)

    # Create target empty for tracking
    target = bpy.data.objects.new(f"{name}_Target", None)
    scene.collection.objects.link(target)
    target.location = Vector(target_location)
    target.empty_display_type = 'SPHERE'
    target.empty_display_size = 0.5

    # Add track-to constraint
    track = camera_object.constraints.new(type="TRACK_TO")
    track.target = target
    track.track_axis = 'TRACK_NEGATIVE_Z'
    track.up_axis = 'UP_Y'

    # Set as active camera
    scene.camera = camera_object

    return {"status": "ok", "camera": camera_object.name, "target": target.name}