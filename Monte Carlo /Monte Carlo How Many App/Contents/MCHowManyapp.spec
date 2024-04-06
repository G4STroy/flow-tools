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

# Post-build code signing and notarization steps
import os

# Path to your 'entitlements.plist' file
entitlements = '/Users/troy.lightfoot/Github Projects/flow-tools/Monte Carlo /Monte Carlo How Many App/Contents/entitlements.plist'

# Developer ID Application identity (replace with your actual identity)
codesign_identity = "Developer ID Application: Troy Lightfoot (g4stroy@gmail.com)"

# Code sign the .app
app_path = os.path.join('dist', 'MCHowManyapp.app')
codesign_command = f"codesign --deep --force --options runtime --entitlements {entitlements} --sign '{codesign_identity}' '{app_path}'"

# Run the codesign command after build
a.binaries.append(('codesign', None, 'EXECUTABLE'))
a.datas.append((entitlements, '.', 'DATA'))

def codesign_app():
    if os.system(codesign_command) == 0:
        print("App signed successfully.")
    else:
        raise Exception("Code signing failed.")

codesign_app()
