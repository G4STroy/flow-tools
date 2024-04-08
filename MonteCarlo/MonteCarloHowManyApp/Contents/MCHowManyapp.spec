import os
import pandas
import numpy
import matplotlib.pyplot
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# Collect all files from the 'Resources' directory and include them in the bundle
resource_dir = '/Users/troy.lightfoot/Github Projects/flow-tools/MonteCarlo/MonteCarloHowManyApp/Contents/Resources'
added_files = [(os.path.join(resource_dir, f), 'Resources') for f in os.listdir(resource_dir) if os.path.isfile(os.path.join(resource_dir, f))]

a = Analysis(['MCHowManyapp.py'],
             pathex=[],
             binaries=[],
             datas=added_files,  # Use the added_files variable here
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
    console=False,  # Set to False if your app doesn't need a console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(exe,
             name='MCHowManyapp.app',
             icon='Resources/MonteCarloHowMany.icns',
             bundle_identifier=None)