# 2016.05.01 15:24:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ChannelComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ChannelComponentMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def isJoined(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isJoined')

    def sendMessage(self, message):
        """
        :param message:
        :return Boolean:
        """
        self._printOverrideError('sendMessage')

    def getHistory(self):
        """
        :return String:
        """
        self._printOverrideError('getHistory')

    def getMessageMaxLength(self):
        """
        :return int:
        """
        self._printOverrideError('getMessageMaxLength')

    def onLinkClick(self, linkCode):
        """
        :param linkCode:
        :return :
        """
        self._printOverrideError('onLinkClick')

    def getLastUnsentMessage(self):
        """
        :return String:
        """
        self._printOverrideError('getLastUnsentMessage')

    def setLastUnsentMessage(self, message):
        """
        :param message:
        :return :
        """
        self._printOverrideError('setLastUnsentMessage')

    def as_setJoinedS(self, flag):
        """
        :param flag:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setJoined(flag)

    def as_addMessageS(self, message):
        """
        :param message:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_addMessage(message)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\channelcomponentmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:56 Støední Evropa (letní èas)
