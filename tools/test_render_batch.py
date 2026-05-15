import sys
import os
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src = os.path.join(root, 'src')
if src not in sys.path:
    sys.path.insert(0, src)

from anim3d.export.render_batch import batch_render

if __name__ == '__main__':
    tasks = [
        {'start': 1, 'end': 3, 'output_path': 'C:/tmp/out', 'scene': None}
    ]
    res = batch_render(tasks)
    print('RESULT:', res)
