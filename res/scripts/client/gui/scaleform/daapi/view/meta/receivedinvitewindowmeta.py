# 2016.05.01 15:22:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ReceivedInviteWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ReceivedInviteWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def acceptInvite(self):
        """
        :return :
        """
        self._printOverrideError('acceptInvite')

    def declineInvite(self):
        """
        :return :
        """
        self._printOverrideError('declineInvite')

    def cancelInvite(self):
        """
        :return :
        """
        self._printOverrideError('cancelInvite')

    def as_setTitleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(value)

    def as_setReceivedInviteInfoS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setReceivedInviteInfo(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\receivedinvitewindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:49 Støední Evropa (letní èas)
