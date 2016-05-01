# 2016.05.01 15:24:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/LobbyChannelWindowMeta.py
from messenger.gui.Scaleform.view.SimpleChannelWindow import SimpleChannelWindow

class LobbyChannelWindowMeta(SimpleChannelWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleChannelWindow
    null
    """

    def as_getMembersDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getMembersDP()

    def as_hideMembersListS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideMembersList()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\lobbychannelwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:57 Støední Evropa (letní èas)
