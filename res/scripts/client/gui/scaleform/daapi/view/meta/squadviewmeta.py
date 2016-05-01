# 2016.05.01 15:22:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SquadViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class SquadViewMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    null
    """

    def leaveSquad(self):
        """
        :return :
        """
        self._printOverrideError('leaveSquad')

    def as_updateBattleTypeInfoS(self, tooltip, isVisible):
        """
        :param tooltip:
        :param isVisible:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateBattleTypeInfo(tooltip, isVisible)

    def as_updateBattleTypeS(self, battleTypeName, isEventEnabled, isNew):
        """
        :param battleTypeName:
        :param isEventEnabled:
        :param isNew:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateBattleType(battleTypeName, isEventEnabled, isNew)

    def as_isFalloutS(self, isFallout):
        """
        :param isFallout:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_isFallout(isFallout)

    def as_updateInviteBtnStateS(self, isEnabled):
        """
        :param isEnabled:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateInviteBtnState(isEnabled)

    def as_setCoolDownForReadyButtonS(self, timer):
        """
        :param timer:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownForReadyButton(timer)

    def as_setSimpleTeamSectionDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSimpleTeamSectionData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\squadviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:51 Støední Evropa (letní èas)
