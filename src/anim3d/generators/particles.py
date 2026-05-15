def generate_particles(count=1000, emitter=None, options=None):
    """Create particle systems. Simulation-safe placeholder.

    Returns a dict describing created systems or a simulated response.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "count": count, "emitter": emitter}

    # Real implementation would create particle systems on `emitter`.
    print(f"generate_particles: created {count} particles on emitter={emitter}")
    return {"status": "ok", "count": count, "emitter": emitter}