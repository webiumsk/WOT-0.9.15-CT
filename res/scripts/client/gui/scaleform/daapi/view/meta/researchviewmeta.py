# 2016.05.01 15:22:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ResearchViewMeta.py
from gui.Scaleform.framework.entities.View import View

class ResearchViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def request4Unlock(self, itemCD, parentID, unlockIdx, xpCost):
        """
        :param itemCD:
        :param parentID:
        :param unlockIdx:
        :param xpCost:
        :return :
        """
        self._printOverrideError('request4Unlock')

    def request4Buy(self, itemCD):
        """
        :param itemCD:
        :return :
        """
        self._printOverrideError('request4Buy')

    def request4Info(self, itemCD, rootCD):
        """
        :param itemCD:
        :param rootCD:
        :return :
        """
        self._printOverrideError('request4Info')

    def showSystemMessage(self, typeString, message):
        """
        :param typeString:
        :param message:
        :return :
        """
        self._printOverrideError('showSystemMessage')

    def as_setNodesStatesS(self, primary, data):
        """
        :param primary:
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setNodesStates(primary, data)

    def as_setNext2UnlockS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setNext2Unlock(data)

    def as_setVehicleTypeXPS(self, xps):
        """
        :param xps:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleTypeXP(xps)

    def as_setInventoryItemsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInventoryItems(data)

    def as_useXMLDumpingS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_useXMLDumping()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\researchviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:50 Støední Evropa (letní èas)
