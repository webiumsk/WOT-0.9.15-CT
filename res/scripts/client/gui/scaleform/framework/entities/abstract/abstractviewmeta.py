# 2016.05.01 15:22:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AbstractViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onFocusIn(self, alias):
        """
        :param alias:
        :return :
        """
        self._printOverrideError('onFocusIn')

    def as_setupContextHintBuilderS(self, builderLnk, data):
        """
        :param builderLnk:
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setupContextHintBuilder(builderLnk, data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\abstractviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:57 Støední Evropa (letní èas)
