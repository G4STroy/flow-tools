# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['MCHowManyapp.py'],
             pathex=[],
             binaries=[],
             datas=[('/Users/troy.lightfoot/Github Projects/flow-tools/Monte Carlo /Monte Carlo How Many App/Contents/Resources/MonteCarloHowMany.icns', '.'),
                     ('/Users/troy.lightfoot/Github Projects/flow-tools/Monte Carlo /Monte Carlo How Many App/Contents/Resources/Monte Carlo How Many User Guide.docx', '.'),
                     ('/Users/troy.lightfoot/Github Projects/flow-tools/Monte Carlo /Monte Carlo How Many App/Contents/Resources/Monte Carlo How Many.xlsx', '.')],
             hiddenimports=["pandas","numpy","matplotlib.pyplot"],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MCHowManyapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          argv_emulation=False,
          target_arch=None,
          icon='/Users/troy.lightfoot/Github Projects/flow-tools/Monte Carlo /Monte Carlo How Many App/Contents/Resources/MonteCarloHowMany.icns'
          )

app = BUNDLE(exe,
             name='MCHowManyapp.app',
             icon='/Users/troy.lightfoot/Github Projects/flow-tools/Monte Carlo /Monte Carlo How Many App/Contents/Resources/MonteCarloHowMany.icns',
             bundle_identifier=None
             )
