def export_video(start_frame=None, end_frame=None, output_path=None, options=None):
    """Export video using the scene's sequencer or render settings.

    Simulation-safe: when not in Blender returns a summary dict.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "start": start_frame, "end": end_frame, "output": output_path}

    scene = bpy.context.scene
    if start_frame is not None:
        scene.frame_start = int(start_frame)
    if end_frame is not None:
        scene.frame_end = int(end_frame)
    if output_path:
        scene.render.filepath = output_path

    bpy.ops.render.render(animation=True)
    return {"status": "rendered", "output": output_path}