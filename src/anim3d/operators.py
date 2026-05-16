try:
    import bpy
    from bpy.types import Operator
    from bpy.props import StringProperty, IntProperty, FloatProperty
except Exception:
    bpy = None
    Operator = object

    def StringProperty(**kwargs):
        return None

    def IntProperty(**kwargs):
        return None

    def FloatProperty(**kwargs):
        return None


class ANIM3D_OT_GenerateMorphing(Operator):
    bl_idname = "anim3d.generate_morphing"
    bl_label = "Generate Morphing"
    bl_options = {"REGISTER", "UNDO"}

    duration: IntProperty(name="Duration", default=120, min=1)

    def execute(self, context):
        from .generators.morphing import generate_morphing

        obj = getattr(context, 'object', None)
        target_names = [obj.name] if obj else None
        result = generate_morphing(targets=target_names, duration=self.duration)

        if hasattr(self, 'report'):
            self.report({"INFO"}, f"Morphing {result['status']}")
        return {'FINISHED'}


class ANIM3D_OT_GenerateParticles(Operator):
    bl_idname = "anim3d.generate_particles"
    bl_label = "Generate Particles"
    bl_options = {"REGISTER", "UNDO"}

    count: IntProperty(name="Count", default=500, min=10)

    def execute(self, context):
        from .generators.particles import generate_particles

        obj = getattr(context, 'object', None)
        emitter_name = obj.name if obj else None
        result = generate_particles(count=self.count, emitter=emitter_name)

        if hasattr(self, 'report'):
            self.report({"INFO"}, f"Particles {result['status']}")
        return {'FINISHED'}


class ANIM3D_OT_SetupCameraRig(Operator):
    bl_idname = "anim3d.setup_camera_rig"
    bl_label = "Setup Camera Rig"
    bl_options = {"REGISTER", "UNDO"}

    rig_name: StringProperty(name="Rig Name", default="Anim3D_Rig")

    def execute(self, context):
        from .generators.camera_rig import setup_camera_rig

        result = setup_camera_rig(name=self.rig_name)
        if hasattr(self, 'report'):
            self.report({"INFO"}, f"Camera rig {result['status']}")
        return {'FINISHED'}


class ANIM3D_OT_GeneratePhysics(Operator):
    bl_idname = "anim3d.generate_physics"
    bl_label = "Generate Physics"
    bl_options = {"REGISTER", "UNDO"}

    duration: IntProperty(name="Duration", default=250, min=1)

    def execute(self, context):
        from .generators.physics import generate_physics

        result = generate_physics(duration=self.duration)
        if hasattr(self, 'report'):
            self.report({"INFO"}, f"Physics {result['status']}")
        return {'FINISHED'}


class ANIM3D_OT_ExportSequence(Operator):
    bl_idname = "anim3d.export_sequence"
    bl_label = "Export Image Sequence"
    bl_options = {"REGISTER", "UNDO"}

    output_dir: StringProperty(name="Output Directory", default="//renders/sequence")
    start_frame: IntProperty(name="Start Frame", default=1, min=1)
    end_frame: IntProperty(name="End Frame", default=250, min=1)

    def execute(self, context):
        from .export.sequence_export import export_sequence

        result = export_sequence(
            start_frame=self.start_frame,
            end_frame=self.end_frame,
            output_dir=self.output_dir,
        )
        if hasattr(self, 'report'):
            self.report({"INFO"}, f"Sequence export {result['status']}")
        return {'FINISHED'}


class ANIM3D_OT_ExportVideo(Operator):
    bl_idname = "anim3d.export_video"
    bl_label = "Export Video"
    bl_options = {"REGISTER", "UNDO"}

    output_path: StringProperty(name="Output Path", default="//renders/video.mp4")
    start_frame: IntProperty(name="Start Frame", default=1, min=1)
    end_frame: IntProperty(name="End Frame", default=250, min=1)

    def execute(self, context):
        from .export.video_export import export_video

        result = export_video(
            start_frame=self.start_frame,
            end_frame=self.end_frame,
            output_path=self.output_path,
        )
        if hasattr(self, 'report'):
            self.report({"INFO"}, f"Video export {result['status']}")
        return {'FINISHED'}


class ANIM3D_OT_GenerateProcedural(Operator):
    bl_idname = "anim3d.generate_procedural"
    bl_label = "Generate Procedural Scene"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        from .generators.procedural import generate_procedural

        result = generate_procedural()
        if hasattr(self, 'report'):
            self.report({"INFO"}, f"Procedural generation {result['status']}")
        return {'FINISHED'}


class ANIM3D_OT_CreateWave(Operator):
    bl_idname = "anim3d.create_wave"
    bl_label = "Create Wave Effect"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        from .effects.wave import create_wave

        result = create_wave()
        if hasattr(self, 'report'):
            self.report({"INFO"}, f"Wave effect {result['status']}")
        return {'FINISHED'}


classes = [
    ANIM3D_OT_GenerateMorphing,
    ANIM3D_OT_GenerateParticles,
    ANIM3D_OT_SetupCameraRig,
    ANIM3D_OT_GeneratePhysics,
    ANIM3D_OT_ExportSequence,
    ANIM3D_OT_ExportVideo,
    ANIM3D_OT_GenerateProcedural,
    ANIM3D_OT_CreateWave,
]


def register():
    if bpy is None:
        return
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    if bpy is None:
        return
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
