# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['MCHowManyapp.py'],
             pathex=[],
             binaries=[],
             datas=[('aaa/MonteCarloHowManyUserGuide.docx', 'aaa'),
                ('Resources/MonteCarloHowMany.icns', 'aaa'),
                ('aaa/Monte Carlo How Many.xlsx', 'aaa'),],
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
          icon='Resources/MonteCarloHowMany.icns'
          )

app = BUNDLE(exe,
             name='MCHowManyapp.app',
             icon='Resources/MonteCarloHowMany.icns',
             bundle_identifier=None
             )
