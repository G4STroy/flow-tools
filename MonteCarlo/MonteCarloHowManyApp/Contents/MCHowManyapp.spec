# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['MCHowManyapp.py'],
    pathex=[],
    binaries=[],
    datas=[('Resources/*', 'Resources')],
    hiddenimports=[
        'pandas', 'numpy', 'matplotlib', 'matplotlib.backends.backend_tkagg',
        'openpyxl', 'openpyxl.workbook', 'openpyxl.worksheet', 'openpyxl.drawing.image'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MCHowManyapp',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MCHowManyapp',
)
app = BUNDLE(
    coll,
    name='MCHowManyapp.app',
    icon='Resources/MonteCarloHowMany.icns',
    bundle_identifier='com.example.MCHowManyApp',
)
