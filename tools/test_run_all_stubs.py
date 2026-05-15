import sys, os
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src = os.path.join(root, 'src')
if src not in sys.path:
    sys.path.insert(0, src)

# Import modules to ensure no syntax errors and call key functions
from anim3d import __init__ as anim3d_init
from anim3d import addon as anim3d_addon
from anim3d import operators as anim3d_ops

from anim3d.generators import morphing, camera_rig, physics, particles
from anim3d.effects import growth, explosion, fracture, dissolve
from anim3d.export import render_batch, sequence_export, video_export

print('Calling register/unregister')
anim3d_init.register()
anim3d_init.unregister()

print('Calling addon register/unregister')
anim3d_addon.register()
anim3d_addon.unregister()

print('Calling operator')
op = anim3d_ops.Anim3DOperator()
print(op.execute())

print('Calling generators')
print(morphing.generate_morphing(['A','B'], duration=10))
print(camera_rig.setup_camera_rig())
print(physics.generate_physics())
print(particles.generate_particles())

print('Calling effects')
print(growth.create_growth('Cube'))
print(explosion.create_explosion((0,0,0), strength=2.0))
print(fracture.create_fracture('Wall', pieces=5))
print(dissolve.create_dissolve('Sphere'))

print('Calling exports')
print(render_batch.batch_render([{'start':1,'end':2,'output_path':None,'scene':None}]))
print(sequence_export.export_sequence(1,2,'/tmp'))
print(video_export.export_video(1,2,'/tmp/out.mp4'))
