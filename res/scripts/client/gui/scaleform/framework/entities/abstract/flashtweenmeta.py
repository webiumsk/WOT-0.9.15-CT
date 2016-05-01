# 2016.05.01 15:22:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/FlashTweenMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class FlashTweenMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def moveOnPositionS(self, percent):
        """
        :param percent:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.moveOnPosition(percent)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\flashtweenmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:58 Støední Evropa (letní èas)
