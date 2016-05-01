# 2016.05.01 15:22:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CheckBoxDialogMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class CheckBoxDialogMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def onCheckBoxChange(self, isSelected):
        """
        :param isSelected:
        :return :
        """
        self._printOverrideError('onCheckBoxChange')

    def as_setCheckBoxLabelS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxLabel(value)

    def as_setCheckBoxSelectedS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxSelected(value)

    def as_setCheckBoxEnabledS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxEnabled(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\checkboxdialogmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:37 Støední Evropa (letní èas)
