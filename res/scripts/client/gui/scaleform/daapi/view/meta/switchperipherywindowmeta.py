# 2016.05.01 15:22:52 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SwitchPeripheryWindowMeta.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta

class SwitchPeripheryWindowMeta(SimpleWindowMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleWindowMeta
    null
    """

    def requestForChange(self, id):
        """
        :param id:
        :return :
        """
        self._printOverrideError('requestForChange')

    def onDropDownOpened(self, opened):
        """
        :param opened:
        :return :
        """
        self._printOverrideError('onDropDownOpened')

    def as_setServerParamsS(self, label, showDropDown):
        """
        :param label:
        :param showDropDown:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setServerParams(label, showDropDown)

    def as_setSelectedIndexS(self, index):
        """
        :param index:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedIndex(index)

    def as_getServersDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getServersDP()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\switchperipherywindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:52 Støední Evropa (letní èas)
