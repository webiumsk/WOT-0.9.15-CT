# 2016.05.01 15:22:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyPageMeta.py
from gui.Scaleform.framework.entities.View import View

class LobbyPageMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def moveSpace(self, x, y, delta):
        """
        :param x:
        :param y:
        :param delta:
        :return :
        """
        self._printOverrideError('moveSpace')

    def getSubContainerType(self):
        """
        :return String:
        """
        self._printOverrideError('getSubContainerType')

    def notifyCursorOver3dScene(self, isOver3dScene):
        """
        :param isOver3dScene:
        :return :
        """
        self._printOverrideError('notifyCursorOver3dScene')

    def as_showHelpLayoutS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showHelpLayout()

    def as_closeHelpLayoutS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_closeHelpLayout()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\lobbypagemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:46 Støední Evropa (letní èas)
