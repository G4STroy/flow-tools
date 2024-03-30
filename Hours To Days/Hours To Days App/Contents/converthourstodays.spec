# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['converthourstodays.py'],
             pathex=[],
             binaries=[],
             datas=[('/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/ConvertedHours.xlsx', '.'),
                     ('/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/HoursConvertTemplate.xlsx', '.'),
                     ('/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/AA Hours To Days Converter Instructions.docx', '.'),
                     ('/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/New icon.icns', '.')],
             hiddenimports=[],
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
          name='converthourstodays',
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
          codesign_identity=None,
          entitlements_file=None,
          icon='/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/New icon.icns'
          )

app = BUNDLE(exe,
             name='converthourstodays.app',
             icon='/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/New icon.icns',
             bundle_identifier=None
             )