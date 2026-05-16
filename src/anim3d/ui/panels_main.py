try:
    import bpy
    from bpy.types import Panel
except Exception:
    bpy = None
    Panel = object


class ANIM3D_PT_MainPanel(Panel):
    bl_label = "Anim3D"
    bl_idname = "ANIM3D_PT_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Anim3D'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Anim3D — Procedural Toolkit")
        layout.operator("anim3d.setup_camera_rig", icon="CAMERA_DATA")
        layout.operator("anim3d.generate_morphing", icon="SHAPEKEY_DATA")
        layout.operator("anim3d.generate_particles", icon="MOD_PARTICLES")
        layout.operator("anim3d.generate_physics", icon="PHYSICS_FORCE")
        layout.operator("anim3d.generate_procedural", icon="MESH_CUBE")
        layout.operator("anim3d.create_wave", icon="MOD_WAVE")
        layout.separator()
        layout.operator("anim3d.export_sequence", icon="RENDER_RESULT")
        layout.operator("anim3d.export_video", icon="SEQUENCE")


def register():
    if bpy is None:
        return
    bpy.utils.register_class(ANIM3D_PT_MainPanel)


def unregister():
    if bpy is None:
        return
    bpy.utils.unregister_class(ANIM3D_PT_MainPanel)
