# 2016.05.01 15:26:35 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/dossiers2/custom/__init__.py


def init():
    from dossiers2.custom.cache import buildCache
    buildCache()
    from dossiers2.custom.dependencies import init as dependencies_init
    dependencies_init()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\dossiers2\custom\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:26:35 St�edn� Evropa (letn� �as)
