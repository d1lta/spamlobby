from cx_Freeze import setup, Executable

executables = [Executable('main.py')]

setup(name='csgospam',
      version='0.0.1',
      description='spam in lobbys',
      executables=executables)