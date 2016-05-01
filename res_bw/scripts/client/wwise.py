# 2016.05.01 15:26:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/WWISE.py
enabled = True
try:
    from _WWISE import *
    import _WWISE
except ImportError:
    print 'WARNING: WWISE support is not enabled.'
    enabled = False

if enabled:
    print 'WARNING: WWISE support IS enabled.'
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\wwise.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:26:47 Støední Evropa (letní èas)
