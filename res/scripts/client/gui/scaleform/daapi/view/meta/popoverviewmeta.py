# 2016.05.01 15:22:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PopOverViewMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class PopOverViewMeta(WrapperViewMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends WrapperViewMeta
    null
    """

    def as_setArrowDirectionS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setArrowDirection(value)

    def as_setArrowPositionS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setArrowPosition(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\popoverviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:47 Støední Evropa (letní èas)
