from setuptools import setup, Extension

pippic = Extension('_pippic', 
        sources = ['src/pippi.c'], 
        )

setup(name='pippi',
        version='1.0b1-3',
        description='Computer music with python',
        url='http://hecanjog.github.com/pippi',

        author='He Can Jog',
        author_email='erik@hecanjog.com',
        license='Public Domain',

        classifiers = [
            'Development Status :: 4 - Beta',
            'Programming Language :: Python :: 2.7',  
        ],

        scripts = ['bin/pippi'],

        keywords = 'music dsp',

        install_requires = [
            'pyaudio',
            'mido',
        ],

        packages=['pippi'],
        ext_modules=[ pippic ],

        data_files=[
            ('pippi', ['pippi/default.config'])
        ],

        zip_safe=False
    )
