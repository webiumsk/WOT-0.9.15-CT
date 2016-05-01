# 2016.05.01 15:22:53 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleInfoMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleInfoMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def getVehicleInfo(self):
        """
        :return :
        """
        self._printOverrideError('getVehicleInfo')

    def onCancelClick(self):
        """
        :return :
        """
        self._printOverrideError('onCancelClick')

    def as_setVehicleInfoS(self, vehicleInfo):
        """
        :param vehicleInfo:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleInfo(vehicleInfo)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\vehicleinfometa.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:53 Støední Evropa (letní èas)
