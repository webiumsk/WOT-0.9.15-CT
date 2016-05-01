# 2016.05.01 15:22:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SlotsPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SlotsPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def getSlotTooltipBody(self, orderID):
        """
        :param orderID:
        :return String:
        """
        self._printOverrideError('getSlotTooltipBody')

    def as_setPanelPropsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelProps(data)

    def as_setSlotsS(self, orders):
        """
        :param orders:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSlots(orders)

    def as_updateSlotS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateSlot(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\slotspanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:51 Støední Evropa (letní èas)
