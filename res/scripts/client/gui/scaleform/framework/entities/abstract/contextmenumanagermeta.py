# 2016.05.01 15:22:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ContextMenuManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ContextMenuManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def requestOptions(self, type, ctx):
        """
        :param type:
        :param ctx:
        :return :
        """
        self._printOverrideError('requestOptions')

    def onOptionSelect(self, optionId):
        """
        :param optionId:
        :return :
        """
        self._printOverrideError('onOptionSelect')

    def onHide(self):
        """
        :return :
        """
        self._printOverrideError('onHide')

    def as_setOptionsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setOptions(data)

    def as_hideS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\contextmenumanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:58 Støední Evropa (letní èas)
