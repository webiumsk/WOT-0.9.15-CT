# 2016.05.01 15:22:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AbstractRallyViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AbstractRallyViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setPyAliasS(self, alias):
        """
        :param alias:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPyAlias(alias)

    def as_getPyAliasS(self):
        """
        :return String:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getPyAlias()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\abstractrallyviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:35 Støední Evropa (letní èas)
