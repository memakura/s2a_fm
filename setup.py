# coding=utf-8

import sys
import json
import os
from cx_Freeze import setup, Executable


name = "s2a_fm"
version = "1.5"
description = 'Arduino Extention for Scratch2.0 Offline Editor'
author = 'MrYsLab (msi installer: memakura)'
url ='https://github.com/MrYsLab/s2a_fm'

# 変更しない
upgrade_code = '{CE9899FD-C244-4C07-8F10-BD911E7183A4}'

# ----------------------------------------------------------------
# セットアップ
# ----------------------------------------------------------------
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "s2a_fm",                    # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]s2a_fm.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     "TARGETDIR",              # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

build_exe_options = {"packages": ["os","serial.win32"],
                    "excludes": [],
                    "includes": [],
                    "include_files": ['xlate.cfg','work/','images/', 'ScratchFiles/']
}
#                    "compressed": True


bdist_msi_options = {'upgrade_code': upgrade_code,
                    'add_to_path': False,
                    'data': msi_data
}

#bdist_mac_options = {"iconfile": 'images/icon.icns'}

options = {
    'build_exe': build_exe_options,
    'bdist_msi': bdist_msi_options
}

# exeの情報
base = None #'Win32GUI' if sys.platform == 'win32' else None
icon = 'images/icon_256x256.ico'

# exe にしたい python ファイルを指定
exe = Executable(script = 's2a_fm_class.py',
                 targetName = 's2a_fm.exe',
                 base = base,
                 icon = icon
                 )
#                 copyDependentFiles = True

# セットアップ
setup(name = name,
      version = version,
      author=author,
      url=url,
      description = description,
      options = options,
      executables = [exe]
      )
