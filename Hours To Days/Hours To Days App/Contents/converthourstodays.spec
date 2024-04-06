# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['converthourstodays.py'],
             pathex=[],
             binaries=[],
             datas=[('/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/ConvertedHours.xlsx', '.'),
                     ('/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/HoursConvertTemplate.xlsx', '.'),
                     ('/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/AA Hours To Days Converter Instructions.docx', '.'),
                     ('/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/Hours To Days Converter.icns', '.')],
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
          codesign_identity="Developer ID Application: Troy Lightfoot (g4stroy@gmail.com)",
          entitlements_file="/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Contents/entitlements.plist",
          icon='/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/Hours To Days Converter.icns'
          )

app = BUNDLE(exe,
             name='converthourstodays.app',
             icon='/Users/troy.lightfoot/Github Projects/flow-tools/Hours To Days/Hours To Days App/Resources/Hours To Days Converter.icns',
             bundle_identifier="com.example.converthourstodays",  # Update with your app's bundle identifier
             plist=dict(
                 CFBundleExecutable="converthourstodays",
                 CFBundleGetInfoString="Created by MyApp",
                 CFBundleIconFile="Hours To Days Converter.icns",
                 CFBundleIdentifier="com.example.converthourstodays",
                 CFBundleInfoDictionaryVersion="6.0",
                 CFBundleName="converthourstodays",
                 CFBundlePackageType="APPL",
                 CFBundleShortVersionString="1.0",
                 CFBundleSignature="????",
                 LSMinimumSystemVersion="10.9",
                 NSPrincipalClass="NSApplication"
             )
             )
