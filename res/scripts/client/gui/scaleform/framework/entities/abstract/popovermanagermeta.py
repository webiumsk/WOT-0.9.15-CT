# 2016.05.01 15:22:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/PopoverManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class PopoverManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def requestShowPopover(self, alias, data):
        """
        :param alias:
        :param data:
        :return :
        """
        self._printOverrideError('requestShowPopover')

    def requestHidePopover(self):
        """
        :return :
        """
        self._printOverrideError('requestHidePopover')

    def as_onPopoverDestroyS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onPopoverDestroy()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\popovermanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:58 Støední Evropa (letní èas)
