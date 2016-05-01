# 2016.05.01 15:24:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ChannelsManagementWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ChannelsManagementWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def getSearchLimitLabel(self):
        """
        :return String:
        """
        self._printOverrideError('getSearchLimitLabel')

    def searchToken(self, token):
        """
        :param token:
        :return :
        """
        self._printOverrideError('searchToken')

    def joinToChannel(self, index):
        """
        :param index:
        :return :
        """
        self._printOverrideError('joinToChannel')

    def createChannel(self, name, usePassword, password, retype):
        """
        :param name:
        :param usePassword:
        :param password:
        :param retype:
        :return :
        """
        self._printOverrideError('createChannel')

    def as_freezSearchButtonS(self, isEnable):
        """
        :param isEnable:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_freezSearchButton(isEnable)

    def as_getDataProviderS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\channelsmanagementwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:56 Støední Evropa (letní èas)
