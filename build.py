from cx_Freeze import setup, Executable

executables = [Executable('main.py')]

setup(name='csgospam',
      version='0.0.3',
      description='spam in lobbys',
      executables=executables)
# python build.py build