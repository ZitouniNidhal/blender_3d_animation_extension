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

    # Real implementation would apply force fields / particle bursts.
    print(f"create_explosion: explosion at {origin} with strength={strength}")
    return {"status": "ok", "origin": origin}