# 2016.05.01 15:22:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MinimapLobbyMeta.py
from gui.Scaleform.daapi.view.meta.MinimapEntityMeta import MinimapEntityMeta

class MinimapLobbyMeta(MinimapEntityMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends MinimapEntityMeta
    null
    """

    def setMap(self, arenaID):
        """
        :param arenaID:
        :return :
        """
        self._printOverrideError('setMap')

    def setMinimapData(self, arenaID, playerTeam, size):
        """
        :param arenaID:
        :param playerTeam:
        :param size:
        :return :
        """
        self._printOverrideError('setMinimapData')

    def as_changeMapS(self, texture):
        """
        :param texture:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_changeMap(texture)

    def as_addPointS(self, x, y, type, color, id):
        """
        :param x:
        :param y:
        :param type:
        :param color:
        :param id:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_addPoint(x, y, type, color, id)

    def as_clearS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_clear()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\minimaplobbymeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:46 Støední Evropa (letní èas)
