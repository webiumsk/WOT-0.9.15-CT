# 2016.05.01 15:22:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleSessionListMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BattleSessionListMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def requestToJoinTeam(self, prbID, prbType):
        """
        :param prbID:
        :param prbType:
        :return :
        """
        self._printOverrideError('requestToJoinTeam')

    def getClientID(self):
        """
        :return Number:
        """
        self._printOverrideError('getClientID')

    def as_refreshListS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_refreshList(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\battlesessionlistmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:37 Støední Evropa (letní èas)
