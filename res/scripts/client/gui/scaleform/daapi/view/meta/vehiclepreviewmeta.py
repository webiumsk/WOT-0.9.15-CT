# 2016.05.01 15:22:53 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewMeta.py
from gui.Scaleform.framework.entities.View import View

class VehiclePreviewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def closeView(self):
        """
        :return :
        """
        self._printOverrideError('closeView')

    def onBackClick(self):
        """
        :return :
        """
        self._printOverrideError('onBackClick')

    def onBuyOrResearchClick(self):
        """
        :return :
        """
        self._printOverrideError('onBuyOrResearchClick')

    def onOpenInfoTab(self, index):
        """
        :param index:
        :return :
        """
        self._printOverrideError('onOpenInfoTab')

    def as_setStaticDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_updateInfoDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateInfoData(data)

    def as_updateVehicleStatusS(self, status):
        """
        :param status:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(status)

    def as_updatePriceS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updatePrice(data)

    def as_updateBuyButtonS(self, enable, label):
        """
        :param enable:
        :param label:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateBuyButton(enable, label)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\vehiclepreviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:54 Støední Evropa (letní èas)
