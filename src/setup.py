from cx_Freeze import setup, Executable
import sys
files = ['img']
includes = ['atexit','sys', 'PySide.QtCore','PySide.QtGui']
base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
        name = 'ConvertMe',
        version = '.1',
        description = 'Allows user to see what I did there.',
        author = 'something',
        options = {'build_exe': {'include_files':files, 'includes':includes}},
        executables = [Executable('main.pyw', base = base,icon = 'img/pic_balance.ico')]
        
  )
