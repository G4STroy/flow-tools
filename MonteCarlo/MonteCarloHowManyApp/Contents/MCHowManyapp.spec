import os
import pandas
import numpy
import matplotlib.pyplot
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# Dynamically determine the resource directory relative to this spec file
spec_dir = os.path.dirname(__file__)
resource_dir = os.path.join(spec_dir, 'Resources')

# Use collect_data_files to automatically collect all files in the Resources directory
added_files = collect_data_files(resource_dir, subdir=None)

a = Analysis(['MCHowManyapp.py'],
             pathex=[],
             binaries=[],
             datas=added_files,  # Use the collected files
             hiddenimports=["pandas", "numpy", "matplotlib.pyplot"],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MCHowManyapp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Adjust according to your need for a console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(exe,
             name='MCHowManyapp.app',
             icon=os.path.join('Resources', 'MonteCarloHowMany.icns'),  # Ensure icon path is also relative
             bundle_identifier=None)