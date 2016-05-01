# 2016.05.01 15:22:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RosterSlotSettingsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class RosterSlotSettingsWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onFiltersUpdate(self, nation, vehicleType, isMain, level, compatibleOnly):
        """
        :param nation:
        :param vehicleType:
        :param isMain:
        :param level:
        :param compatibleOnly:
        :return :
        """
        self._printOverrideError('onFiltersUpdate')

    def requestVehicleFilters(self):
        """
        :return :
        """
        self._printOverrideError('requestVehicleFilters')

    def submitButtonHandler(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('submitButtonHandler')

    def cancelButtonHandler(self):
        """
        :return :
        """
        self._printOverrideError('cancelButtonHandler')

    def as_setVehicleSelectionS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleSelection(data)

    def as_setRangeSelectionS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRangeSelection(data)

    def as_resetSelectionS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_resetSelection()

    def as_selectTabS(self, index):
        """
        :param index:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_selectTab(index)

    def as_setListDataS(self, listData):
        """
        :param listData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setListData(listData)

    def as_setStaticDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setRosterLimitsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRosterLimits(data)

    def as_updateVehicleFiltersS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleFilters(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\rosterslotsettingswindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:50 Støední Evropa (letní èas)
