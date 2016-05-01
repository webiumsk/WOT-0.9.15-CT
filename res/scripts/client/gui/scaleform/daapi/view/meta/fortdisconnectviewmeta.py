# 2016.05.01 15:22:43 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortDisconnectViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortDisconnectViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setWarningTextsS(self, warningTxt, warningDescTxt):
        """
        :param warningTxt:
        :param warningDescTxt:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWarningTexts(warningTxt, warningDescTxt)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortdisconnectviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:43 Støední Evropa (letní èas)
