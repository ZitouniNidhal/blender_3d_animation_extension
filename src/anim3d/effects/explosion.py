def create_explosion(origin=None, strength=1.0, options=None):
    """Create an explosion effect at `origin`.

    Simulation-safe placeholder returning a summary when `bpy` is not present.
    """
    try:
        import bpy
    except Exception:
        bpy = None

    if bpy is None:
        return {"status": "simulated", "origin": origin, "strength": strength}

    # Real implementation would apply force fields / particle bursts.
    print(f"create_explosion: explosion at {origin} with strength={strength}")
    return {"status": "ok", "origin": origin}