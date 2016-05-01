# 2016.05.01 15:22:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseRallyListViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyView import BaseRallyView

class BaseRallyListViewMeta(BaseRallyView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyView
    null
    """

    def getRallyDetails(self, index):
        """
        :param index:
        :return Object:
        """
        self._printOverrideError('getRallyDetails')

    def as_selectByIndexS(self, index):
        """
        :param index:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_selectByIndex(index)

    def as_selectByIDS(self, rallyID):
        """
        :param rallyID:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_selectByID(rallyID)

    def as_getSearchDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()

    def as_setDetailsS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDetails(value)

    def as_setVehiclesTitleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesTitle(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\baserallylistviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:36 Støední Evropa (letní èas)
