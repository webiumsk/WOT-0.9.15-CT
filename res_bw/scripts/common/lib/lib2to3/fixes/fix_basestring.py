# 2016.05.01 15:30:48 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_basestring.py
"""Fixer for basestring -> str."""
from .. import fixer_base
from ..fixer_util import Name

class FixBasestring(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "'basestring'"

    def transform(self, node, results):
        return Name(u'str', prefix=node.prefix)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_basestring.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:30:48 St�edn� Evropa (letn� �as)
