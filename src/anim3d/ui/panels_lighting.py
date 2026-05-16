"""
Lighting UI Panel for Anim3D
Professional UI for controlling and applying lighting presets.
"""

try:
    import bpy
    from bpy.types import Panel, Operator
    from bpy.props import StringProperty, FloatProperty
except Exception:
    bpy = None
    Panel = object
    Operator = object

    def StringProperty(**kwargs):
        return None

    def FloatProperty(**kwargs):
        return None


class ANIM3D_OT_ApplyLightingPreset(Operator):
    """Apply a lighting preset to the scene."""

    bl_idname = "anim3d.apply_lighting_preset"
    bl_label = "Apply Lighting Preset"
    bl_options = {"REGISTER", "UNDO"}

    preset: StringProperty(default="STUDIO")

    def execute(self, context):
        try:
            from .lighting import setup_three_point_lighting

            result = setup_three_point_lighting(preset=self.preset)

            if result["status"] == "ok":
                self.report(
                    {"INFO"},
                    f"✓ {self.preset} lighting created: {', '.join(result['lights_created'])}",
                )
                return {"FINISHED"}
            self.report({"ERROR"}, result.get("message", "Unknown error"))
            return {"CANCELLED"}

        except Exception as e:
            self.report({"ERROR"}, f"Lighting setup failed: {str(e)}")
            return {"CANCELLED"}


class ANIM3D_OT_ApplyDynamicLighting(Operator):
    """Apply animated dynamic lighting."""

    bl_idname = "anim3d.apply_dynamic_lighting"
    bl_label = "Add Dynamic Lights"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        try:
            from .lighting import setup_dynamic_lighting

            intensity_curve = [
                (1, 1.0),
                (125, 2.0),
                (250, 1.0),
            ]

            result = setup_dynamic_lighting(
                intensity_curve=intensity_curve,
                frame_start=1,
                frame_end=250,
            )

            if result["status"] == "ok":
                self.report({"INFO"}, f"✓ Dynamic lighting created: {result['keyframes_set']} keyframes")
                return {"FINISHED"}
            self.report({"ERROR"}, result.get("message", "Unknown error"))
            return {"CANCELLED"}

        except Exception as e:
            self.report({"ERROR"}, f"Dynamic lighting failed: {str(e)}")
            return {"CANCELLED"}


class ANIM3D_OT_ApplyAmbientLighting(Operator):
    """Configure ambient world lighting."""

    bl_idname = "anim3d.apply_ambient_lighting"
    bl_label = "Configure Ambient"
    bl_options = {"REGISTER", "UNDO"}

    ambient_energy: FloatProperty(
        name="Ambient Energy",
        description="World ambient light strength",
        default=0.5,
        min=0.0,
        max=5.0,
    )

    def execute(self, context):
        try:
            from .lighting import setup_ambient_lighting

            result = setup_ambient_lighting(energy=self.ambient_energy)

            if result["status"] == "ok":
                self.report({"INFO"}, f"✓ Ambient lighting configured (energy: {self.ambient_energy})")
                return {"FINISHED"}
            self.report({"ERROR"}, result.get("message", "Unknown error"))
            return {"CANCELLED"}

        except Exception as e:
            self.report({"ERROR"}, f"Ambient setup failed: {str(e)}")
            return {"CANCELLED"}


class ANIM3D_PT_LightingPanel(Panel):
    """Main lighting panel in the Anim3D sidebar."""

    bl_label = "💡 Lighting"
    bl_idname = "ANIM3D_PT_lighting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Anim3D"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        layout.label(text="Professional Lighting Presets", icon="LIGHT_SUN")

        box = layout.box()
        box.label(text="🏢 Studio", icon="LIGHTPROBE_CUBEMAP")
        box.operator("anim3d.apply_lighting_preset", text="Studio Lighting", icon="LIGHT_SUN").preset = "STUDIO"
        box.operator("anim3d.apply_lighting_preset", text="Outdoor Lighting", icon="LIGHT_HEMI").preset = "OUTDOOR"

        box = layout.box()
        box.label(text="🎬 Dramatic", icon="LIGHT_SPOT")
        box.operator("anim3d.apply_lighting_preset", text="Dramatic Setup", icon="LIGHT_SPOT").preset = "DRAMATIC"
        box.operator("anim3d.apply_lighting_preset", text="Soft Lighting", icon="LIGHT_AREA").preset = "SOFT"

        box = layout.box()
        box.label(text="✨ Neon", icon="COLOR_RED")
        box.operator("anim3d.apply_lighting_preset", text="Neon Setup", icon="NODE_PHYSICS_WARP").preset = "NEON"

        box = layout.box()
        box.label(text="⏱️ Animation", icon="ACTION")
        box.operator("anim3d.apply_dynamic_lighting", text="Add Dynamic Lights", icon="ANIM")

        box = layout.box()
        box.label(text="🌍 Ambient", icon="WORLD")
        props = box.operator("anim3d.apply_ambient_lighting", text="Configure Ambient", icon="WORLD")
        props.ambient_energy = 0.5


def register():
    if bpy is None:
        return
    bpy.utils.register_class(ANIM3D_OT_ApplyLightingPreset)
    bpy.utils.register_class(ANIM3D_OT_ApplyDynamicLighting)
    bpy.utils.register_class(ANIM3D_OT_ApplyAmbientLighting)
    bpy.utils.register_class(ANIM3D_PT_LightingPanel)


def unregister():
    if bpy is None:
        return
    bpy.utils.unregister_class(ANIM3D_PT_LightingPanel)
    bpy.utils.unregister_class(ANIM3D_OT_ApplyAmbientLighting)
    bpy.utils.unregister_class(ANIM3D_OT_ApplyDynamicLighting)
    bpy.utils.unregister_class(ANIM3D_OT_ApplyLightingPreset)
