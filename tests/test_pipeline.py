from tools.run_pipeline import run_pipeline
import os


def test_pipeline_runs_simulation():
    preset = os.path.join(os.path.dirname(__file__), '..', 'assets', 'presets', 'sample_preset.json')
    result = run_pipeline(preset)
    assert isinstance(result, dict)
    # Check some expected keys exist
    assert 'rig' in result
    assert 'morph' in result
    assert 'growth' in result
    assert 'explosion' in result
    assert 'fracture' in result
    assert 'dissolve' in result
    assert 'sequence' in result
    assert result['sequence']['status'] in ('simulated', 'rendered')


if __name__ == '__main__':
    print('Running pipeline test (manual)')
    test_pipeline_runs_simulation()
    print('OK')
