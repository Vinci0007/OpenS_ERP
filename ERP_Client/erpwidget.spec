# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['erpwidget.py'],
    pathex=['E:\\0001_Work_New\\012_ZGHK\\QT_ERP_Python\\ERP_Python_qt'],
    binaries=[],
    datas=[('E:\\0001_Work_New\\012_ZGHK\\QT_ERP_Python\\ERP_Python_qt\\Resource', 'Resource')],
    hiddenimports=[
        'E:\\0001_Work_New\\012_ZGHK\\QT_ERP_Python\\ERP_Python_qt\\Resource\\Addons',
        'E:\\0001_Work_New\\012_ZGHK\\QT_ERP_Python\\ERP_Python_qt\\Resource\\Addons\\__init__.py',
        'E:\\0001_Work_New\\012_ZGHK\\QT_ERP_Python\\ERP_Python_qt\\Resource\\CommonTools',
        'E:\\0001_Work_New\\012_ZGHK\\QT_ERP_Python\\ERP_Python_qt\\Resource\\CommonTools\\__init__.py',
        ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='erpwidget',
    debug=False,
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
    name='erpwidget',
)


