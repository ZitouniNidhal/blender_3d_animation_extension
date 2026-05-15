import json
import os
import sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src = os.path.join(root, 'src')
if src not in sys.path:
    sys.path.insert(0, src)

from anim3d.generators import camera_rig, morphing, particles, physics
from anim3d.effects import growth, explosion, fracture, dissolve
from anim3d.export import render_batch, sequence_export, video_export


def run_pipeline(preset_path=None):
    """Run a simple animation pipeline using functions in the package.

    This runner is simulation-safe and useful for automated pipelines or CI.
    """
    preset = {}
    if preset_path and os.path.exists(preset_path):
        with open(preset_path, 'r', encoding='utf-8') as f:
            preset = json.load(f)

    report = {}

    report['rig'] = camera_rig.setup_camera_rig(preset.get('rig_name', 'Anim3D_Rig'))
    report['morph'] = morphing.generate_morphing(preset.get('morph_targets'), preset.get('morph_duration', 100))
    report['particles'] = particles.generate_particles(preset.get('particles_count', 1000), preset.get('particles_emitter'))
    report['physics'] = physics.generate_physics(preset.get('physics_duration', 250))

    report['growth'] = growth.create_growth(preset.get('growth_target'), preset.get('growth_duration', 50))
    report['explosion'] = explosion.create_explosion(preset.get('explosion_origin'), preset.get('explosion_strength', 1.0))
    report['fracture'] = fracture.create_fracture(preset.get('fracture_target'), preset.get('fracture_pieces', 10))
    report['dissolve'] = dissolve.create_dissolve(preset.get('dissolve_target'), preset.get('dissolve_duration', 30))

    # Exports
    report['sequence'] = sequence_export.export_sequence(preset.get('start_frame', 1), preset.get('end_frame', 250), preset.get('output_dir'))
    report['video'] = video_export.export_video(preset.get('start_frame', 1), preset.get('end_frame', 250), preset.get('video_output'))

    # Optionally batch renders
    batch_tasks = preset.get('batch_tasks')
    if batch_tasks:
        report['batch'] = render_batch.batch_render(batch_tasks)

    return report


if __name__ == '__main__':
    preset = None
    if len(sys.argv) > 1:
        preset = sys.argv[1]
    result = run_pipeline(preset)
    print('Pipeline result:')
    print(result)
