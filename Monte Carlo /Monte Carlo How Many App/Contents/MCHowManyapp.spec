block_cipher = None

a = Analysis(
    ['MCHowManyapp.py'],  # Correct path to your main Python script
    pathex=[],
    binaries=[],
    datas=[
        # Relative paths to the resources based on the structure in the provided screenshot
        ('Resources/monteimage.jpeg', 'Resources'),
        ('Resources/Monte Carlo How Many.xlsx', 'Resources'),
        ('Resources/Monte Carlo How Many User Guide.docx', 'Resources')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False
)
pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Monte Carlo How Many',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    # Relative path to the icon file
    icon='Monte Carlo How Many App/Contents/Resources/MCHWicon.icns',
)
app = BUNDLE(
    exe,
    name='Monte Carlo How Many.app',
    # Relative path to the icon file
    icon='Resources/MCHWicon.icns',
    bundle_identifier='com.example.montecarlohowmany'
)
