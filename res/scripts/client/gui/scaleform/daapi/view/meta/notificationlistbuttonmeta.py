# 2016.05.01 15:22:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationListButtonMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class NotificationListButtonMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def handleClick(self):
        """
        :return :
        """
        self._printOverrideError('handleClick')

    def as_setStateS(self, isBlinking):
        """
        :param isBlinking:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setState(isBlinking)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\notificationlistbuttonmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:47 Støední Evropa (letní èas)
