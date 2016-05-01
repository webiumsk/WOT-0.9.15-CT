# 2016.05.01 15:22:48 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileTechniquePageMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileTechnique import ProfileTechnique

class ProfileTechniquePageMeta(ProfileTechnique):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ProfileTechnique
    null
    """

    def setIsInHangarSelected(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('setIsInHangarSelected')

    def as_setSelectedVehicleIntCDS(self, index):
        """
        :param index:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedVehicleIntCD(index)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\profiletechniquepagemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:48 Støední Evropa (letní èas)
