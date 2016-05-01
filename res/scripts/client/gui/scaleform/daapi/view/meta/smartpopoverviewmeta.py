# 2016.05.01 15:22:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SmartPopOverViewMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractPopOverView import AbstractPopOverView

class SmartPopOverViewMeta(AbstractPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractPopOverView
    null
    """

    def as_setPositionKeyPointS(self, valX, valY):
        """
        :param valX:
        :param valY:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPositionKeyPoint(valX, valY)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\smartpopoverviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:51 Støední Evropa (letní èas)
