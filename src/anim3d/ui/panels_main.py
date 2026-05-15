import bpy

class ANIM3D_PT_MainPanel(bpy.types.Panel):
    bl_label = "Anim3D"
    bl_idname = "ANIM3D_PT_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Anim3D'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Anim3D — Generators")
        layout.operator("anim3d.generate_morphing", text="Generate Morphing")
        layout.operator("anim3d.generate_particles", text="Generate Particles")


def register():
    bpy.utils.register_class(ANIM3D_PT_MainPanel)


def unregister():
    bpy.utils.unregister_class(ANIM3D_PT_MainPanel)
