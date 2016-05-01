# 2016.05.01 15:22:42 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortClanBattleListMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyListView import BaseRallyListView

class FortClanBattleListMeta(BaseRallyListView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyListView
    null
    """

    def as_setClanBattleDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanBattleData(data)

    def as_upateClanBattlesCountS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_upateClanBattlesCount(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortclanbattlelistmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:42 Støední Evropa (letní èas)
