# 2016.05.01 15:22:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ResearchPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ResearchPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def goToResearch(self):
        """
        :return :
        """
        self._printOverrideError('goToResearch')

    def as_updateCurrentVehicleS(self, name, type, vDescription, earnedXP, isElite, isPremIGR):
        """
        :param name:
        :param type:
        :param vDescription:
        :param earnedXP:
        :param isElite:
        :param isPremIGR:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateCurrentVehicle(name, type, vDescription, earnedXP, isElite, isPremIGR)

    def as_setEarnedXPS(self, earnedXP):
        """
        :param earnedXP:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setEarnedXP(earnedXP)

    def as_setEliteS(self, isElite):
        """
        :param isElite:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setElite(isElite)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\researchpanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:50 Støední Evropa (letní èas)
