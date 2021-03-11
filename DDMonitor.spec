# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# PyQt5 exclude modules
pyqt_exc = [
    'PyQt5.QtNetwork',
    'PyQt5.QtQml',
    'PyQt5.QAxContainer',
    'PyQt5.QtBluetooth',
    'PyQt5.QtDBus',
    'PyQt5.QtDesigner',
    'PyQt5.QtHelp',
    'PyQt5.QtMultimedia',
    'PyQt5.QtMultimediaWidgets',
    'PyQt5.QtNetworkAuth',
    'PyQt5.QtNfc',
    'PyQt5.QtOpenGL',
    'PyQt5.QtPositioning',
    'PyQt5.QtLocation',
    'PyQt5.QtPrintSupport',
    'PyQt5.QtQuick',
    'PyQt5.QtQuick3D',
    'PyQt5.QtQuickWidgets',
    'PyQt5.QtRemoteObjects',
    'PyQt5.QtSensors',
    'PyQt5.QtSerialPort',
    'PyQt5.QtSql',
    'PyQt5.QtSvg',
    'PyQt5.QtTest',
    'PyQt5.QtTextToSpeech',
    'PyQt5.QtWebChannel',
    'PyQt5.QtWebSockets',
    'PyQt5.QtWinExtras',
    'PyQt5.QtXml',
    'PyQt5.QtXmlPatterns'
]


a = Analysis(['DD监控室.py'],
             pathex=[],
             binaries=[],
             datas=[
                ('utils/ascii.txt', '.'),
                ('utils/help.html', '.'),
                ('utils/splash.jpg', 'utils'),
                ('utils/vtb.csv', 'utils'),
                ('scripts/run.bat', '.'),
             ],
             hiddenimports=[],
             hookspath=['hooks'],
             runtime_hooks=[],
             excludes=pyqt_exc,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='DDMonitor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          icon='favicon.ico',
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='DDMonitor')
