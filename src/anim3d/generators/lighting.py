"""
Lighting Generator Module for Anim3D
Professional lighting system with 5 presets, dynamic animation, and ambient control.
Works both inside Blender and as standalone Python simulation.
"""

import math
from typing import Dict, List, Tuple, Optional


def validate_preset(preset: str) -> bool:
    """Validate that preset name is supported."""
    valid_presets = {"STUDIO", "OUTDOOR", "DRAMATIC", "SOFT", "NEON"}
    return preset.upper() in valid_presets


def get_light_positions(preset: str) -> Dict[str, Tuple[float, float, float]]:
    """Get light positions for a given preset.
    
    Returns dict with 'key', 'fill', 'back' positions in (x, y, z) format.
    """
    positions = {
        "STUDIO": {
            "key": (5.0, -5.0, 7.0),
            "fill": (-4.0, 3.0, 4.0),
            "back": (0.0, -6.0, 3.0),
        },
        "OUTDOOR": {
            "key": (10.0, 5.0, 15.0),
            "fill": (-3.0, -2.0, 2.0),
            "back": (0.0, -8.0, 5.0),
        },
        "DRAMATIC": {
            "key": (4.0, -6.0, 8.0),
            "fill": (-6.0, 4.0, 2.0),
            "back": (1.0, -7.0, 4.0),
        },
        "SOFT": {
            "key": (3.0, -3.0, 6.0),
            "fill": (-3.0, 3.0, 5.0),
            "back": (0.0, -5.0, 3.0),
        },
        "NEON": {
            "key": (6.0, -4.0, 6.0),
            "fill": (-5.0, 5.0, 4.0),
            "back": (2.0, -5.0, 5.0),
        },
    }
    return positions.get(preset.upper(), positions["STUDIO"])


def get_light_colors(preset: str) -> Dict[str, Tuple[float, float, float]]:
    """Get light colors (RGB) for a given preset."""
    colors = {
        "STUDIO": {
            "key": (1.0, 1.0, 1.0),
            "fill": (0.9, 0.95, 1.0),
            "back": (0.8, 0.8, 1.0),
        },
        "OUTDOOR": {
            "key": (1.0, 0.98, 0.95),
            "fill": (0.7, 0.85, 1.0),
            "back": (0.8, 0.9, 1.0),
        },
        "DRAMATIC": {
            "key": (1.0, 1.0, 1.0),
            "fill": (0.3, 0.3, 0.4),
            "back": (1.0, 0.7, 0.5),
        },
        "SOFT": {
            "key": (1.0, 0.95, 0.9),
            "fill": (0.95, 0.95, 1.0),
            "back": (0.9, 0.9, 0.95),
        },
        "NEON": {
            "key": (0.0, 1.0, 1.0),
            "fill": (1.0, 0.0, 1.0),
            "back": (1.0, 1.0, 0.0),
        },
    }
    return colors.get(preset.upper(), colors["STUDIO"])


def get_light_energies(preset: str) -> Dict[str, float]:
    """Get light energy (intensity) values for a given preset."""
    energies = {
        "STUDIO": {"key": 2.5, "fill": 0.8, "back": 1.2},
        "OUTDOOR": {"key": 3.0, "fill": 1.0, "back": 1.5},
        "DRAMATIC": {"key": 3.5, "fill": 0.3, "back": 1.0},
        "SOFT": {"key": 1.8, "fill": 1.5, "back": 1.0},
        "NEON": {"key": 2.0, "fill": 1.5, "back": 1.8},
    }
    return energies.get(preset.upper(), energies["STUDIO"])


def get_light_types(preset: str) -> Dict[str, str]:
    """Get light types for each light in the preset."""
    types = {
        "STUDIO": {"key": "SUN", "fill": "AREA", "back": "POINT"},
        "OUTDOOR": {"key": "SUN", "fill": "AREA", "back": "SUN"},
        "DRAMATIC": {"key": "SPOT", "fill": "AREA", "back": "POINT"},
        "SOFT": {"key": "AREA", "fill": "AREA", "back": "AREA"},
        "NEON": {"key": "SPOT", "fill": "POINT", "back": "POINT"},
    }
    return types.get(preset.upper(), types["STUDIO"])


def setup_three_point_lighting(
    preset: str = "STUDIO",
    target: Optional[str] = None,
    scale: float = 1.0,
) -> Dict:
    """Set up professional three-point lighting.
    
    Args:
        preset: One of 'STUDIO', 'OUTDOOR', 'DRAMATIC', 'SOFT', 'NEON'
        target: Optional target object name to light
        scale: Scale factor for light distances (default 1.0)
    
    Returns:
        Dict with status and creation details
    """
    try:
        import bpy
    except ImportError:
        bpy = None

    # Validate preset
    preset_upper = preset.upper()
    if not validate_preset(preset_upper):
        return {
            "status": "error",
            "message": f"Invalid preset '{preset}'. Valid options: STUDIO, OUTDOOR, DRAMATIC, SOFT, NEON",
        }

    if bpy is None:
        # Simulation mode (outside Blender)
        return {
            "status": "simulated",
            "preset": preset_upper,
            "lights_created": ["Key", "Fill", "Back"],
            "message": f"Simulated {preset_upper} three-point lighting setup",
        }

    # Real Blender implementation
    try:
        positions = get_light_positions(preset_upper)
        colors = get_light_colors(preset_upper)
        energies = get_light_energies(preset_upper)
        types = get_light_types(preset_upper)

        lights_created = []
        light_objects = {}

        # Create lights
        for light_name in ["key", "fill", "back"]:
            # Create light data
            light_data = bpy.data.lights.new(
                name=f"Anim3D_{preset_upper}_{light_name.capitalize()}",
                type=types[light_name],
            )

            # Set light properties
            light_data.energy = energies[light_name]
            if hasattr(light_data, "color"):
                light_data.color = colors[light_name]

            # Set light-specific properties
            if types[light_name] == "SPOT":
                light_data.spot_size = math.radians(45)
                light_data.spot_blend = 0.15
            elif types[light_name] == "AREA":
                light_data.size = 2.0 * scale
            elif types[light_name] == "SUN":
                light_data.angle = math.radians(0.5)

            # Create light object
            light_obj = bpy.data.objects.new(
                name=f"Light_{preset_upper}_{light_name.capitalize()}",
                object_data=light_data,
            )

            # Set position
            pos = positions[light_name]
            light_obj.location = (pos[0] * scale, pos[1] * scale, pos[2] * scale)

            # Link to scene
            scene = bpy.context.scene
            bpy.context.collection.objects.link(light_obj)

            lights_created.append(light_name.capitalize())
            light_objects[light_name] = light_obj

        return {
            "status": "ok",
            "preset": preset_upper,
            "lights_created": lights_created,
            "light_objects": light_objects,
            "message": f"Successfully created {preset_upper} three-point lighting",
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create lighting: {str(e)}",
        }


def setup_dynamic_lighting(
    intensity_curve: Optional[List[Tuple[int, float]]] = None,
    color_curve: Optional[List[Tuple[int, Tuple[float, float, float]]]] = None,
    frame_start: int = 1,
    frame_end: int = 250,
    light_index: int = 0,
) -> Dict:
    """Create animated dynamic lighting with keyframes.
    
    Args:
        intensity_curve: List of (frame, intensity) tuples for animation
        color_curve: List of (frame, (r,g,b)) tuples for color animation
        frame_start: Start frame for animation
        frame_end: End frame for animation
        light_index: Which light to animate (0=key, 1=fill, 2=back)
    
    Returns:
        Dict with status and keyframe information
    """
    try:
        import bpy
    except ImportError:
        bpy = None

    if intensity_curve is None:
        intensity_curve = [
            (frame_start, 1.0),
            (frame_end // 2, 2.0),
            (frame_end, 1.0),
        ]

    if bpy is None:
        # Simulation mode
        return {
            "status": "simulated",
            "keyframes_set": len(intensity_curve) + (len(color_curve) if color_curve else 0),
            "frame_range": (frame_start, frame_end),
            "message": "Simulated dynamic lighting setup",
        }

    try:
        # Real implementation
        scene = bpy.context.scene
        
        # Find existing lights or create new one
        lights = [obj for obj in scene.objects if obj.type == "LIGHT"]
        if not lights:
            return {
                "status": "error",
                "message": "No lights found in scene. Create lights first.",
            }

        light_obj = lights[min(light_index, len(lights) - 1)]
        light_data = light_obj.data

        keyframes_set = 0

        # Set intensity keyframes
        if intensity_curve:
            for frame, intensity in intensity_curve:
                light_data.energy = intensity
                light_data.keyframe_insert(data_path="energy", frame=frame)
                keyframes_set += 1

        # Set color keyframes
        if color_curve:
            for frame, color in color_curve:
                light_data.color = color
                light_data.keyframe_insert(data_path="color", frame=frame)
                keyframes_set += 1

        # Set frame range
        scene.frame_start = frame_start
        scene.frame_end = frame_end

        return {
            "status": "ok",
            "keyframes_set": keyframes_set,
            "frame_range": (frame_start, frame_end),
            "light_object": light_obj.name,
            "message": f"Created {keyframes_set} animation keyframes",
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create dynamic lighting: {str(e)}",
        }


def setup_ambient_lighting(
    energy: float = 0.5,
    color: Tuple[float, float, float] = (1.0, 1.0, 1.0),
    use_nishita_sky: bool = False,
) -> Dict:
    """Configure world ambient lighting.
    
    Args:
        energy: Ambient light strength (0.0 to 5.0)
        color: RGB color tuple (0.0 to 1.0 each)
        use_nishita_sky: Use Nishita Sky Model for realistic sky
    
    Returns:
        Dict with configuration status
    """
    try:
        import bpy
    except ImportError:
        bpy = None

    if bpy is None:
        # Simulation mode
        return {
            "status": "simulated",
            "ambient_energy": energy,
            "ambient_color": color,
            "message": "Simulated ambient lighting configuration",
        }

    try:
        # Real implementation
        world = bpy.context.scene.world
        
        # Configure background shader
        if world.use_nodes:
            nodes = world.node_tree.nodes
            
            # Find or create Background node
            bg_node = None
            for node in nodes:
                if node.type == "BACKGROUND":
                    bg_node = node
                    break
            
            if not bg_node:
                # Create background shader
                bg_node = nodes.new(type="ShaderNodeBackground")
            
            # Set background properties
            if hasattr(bg_node, "inputs"):
                bg_node.inputs["Color"].default_value = (color[0], color[1], color[2], 1.0)
                bg_node.inputs["Strength"].default_value = energy
        else:
            # Fallback for non-node rendering
            world.ambient_color = color

        return {
            "status": "ok",
            "ambient_energy": energy,
            "ambient_color": color,
            "nishita_sky": use_nishita_sky,
            "message": f"Ambient lighting configured (energy: {energy})",
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to configure ambient lighting: {str(e)}",
        }


def reset_lighting() -> Dict:
    """Remove all Anim3D lights from the scene.
    
    Returns:
        Dict with cleanup status
    """
    try:
        import bpy
    except ImportError:
        bpy = None

    if bpy is None:
        return {
            "status": "simulated",
            "message": "Simulated lighting reset",
        }

    try:
        scene = bpy.context.scene
        lights_removed = 0

        # Find and remove all Anim3D lights
        for obj in list(scene.objects):
            if obj.type == "LIGHT" and "Anim3D" in obj.name:
                bpy.data.objects.remove(obj, do_unlink=True)
                lights_removed += 1

        return {
            "status": "ok",
            "lights_removed": lights_removed,
            "message": f"Removed {lights_removed} Anim3D lights",
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to reset lighting: {str(e)}",
        }


# List of all available presets
AVAILABLE_PRESETS = [
    "STUDIO",
    "OUTDOOR",
    "DRAMATIC",
    "SOFT",
    "NEON",
]

# Preset descriptions
PRESET_DESCRIPTIONS = {
    "STUDIO": "Professional three-point lighting for product photography and controlled environments.",
    "OUTDOOR": "Natural daylight with sky fill for outdoor scenes and landscapes.",
    "DRAMATIC": "High-contrast lighting for thriller, suspense, and moody scenes.",
    "SOFT": "Flattering, shadowless lighting for beauty, interviews, and gentle portraits.",
    "NEON": "Futuristic colored lights for sci-fi, music videos, and artistic scenes.",
}
