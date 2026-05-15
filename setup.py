from setuptools import setup, find_packages

setup(
    name='anim3d',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'anim3d=anim3d.__main__:main'
        ]
    },
)