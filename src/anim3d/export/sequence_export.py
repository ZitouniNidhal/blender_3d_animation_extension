def export_sequence(start_frame=None, end_frame=None, output_dir=None, options=None):
    """Export an image sequence between start_frame and end_frame.

    Simulation-safe: when `bpy` is unavailable returns a summary dict.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "start": start_frame, "end": end_frame, "output": output_dir}

    scene = bpy.context.scene
    if start_frame is not None:
        scene.frame_start = int(start_frame)
    if end_frame is not None:
        scene.frame_end = int(end_frame)
    if output_dir:
        scene.render.filepath = output_dir

    bpy.ops.render.render(animation=True)
    return {"status": "rendered", "output": output_dir}