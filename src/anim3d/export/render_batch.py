def batch_render(tasks):
    """Perform batch renders for a list of tasks.

    Each task is a dict with keys:
      - 'start' (int) : start frame (optional)
      - 'end' (int) : end frame (optional)
      - 'output_path' (str) : render output path (optional)
      - 'scene' (str) : scene name to use (optional)

    If running inside Blender (`bpy` available) this will perform real renders.
    Otherwise it will simulate the actions and return a report list.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if not isinstance(tasks, (list, tuple)):
        raise TypeError("tasks must be a list or tuple of task dicts")

    results = []
    for task in tasks:
        start = task.get("start")
        end = task.get("end")
        out_path = task.get("output_path")
        scene_name = task.get("scene")

        if bpy:
            scene = bpy.data.scenes.get(scene_name) if scene_name else bpy.context.scene
            if scene is None:
                results.append({"task": task, "status": "scene_not_found"})
                continue

            if start is not None:
                scene.frame_start = int(start)
            if end is not None:
                scene.frame_end = int(end)
            if out_path:
                scene.render.filepath = out_path

            bpy.ops.render.render(animation=True)
            results.append({"task": task, "status": "rendered"})
        else:
            print(f"[simulated] render task: start={start} end={end} output={out_path} scene={scene_name}")
            results.append({"task": task, "status": "simulated"})

    return results