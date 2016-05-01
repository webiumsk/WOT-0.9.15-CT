# 2016.05.01 15:22:52 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StoreViewMeta.py
from gui.Scaleform.framework.entities.View import View

class StoreViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def onClose(self):
        """
        :return :
        """
        self._printOverrideError('onClose')

    def onTabChange(self, tabId):
        """
        :param tabId:
        :return :
        """
        self._printOverrideError('onTabChange')

    def as_showStorePageS(self, viewAlias):
        """
        :param viewAlias:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showStorePage(viewAlias)

    def as_initS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\storeviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:52 Støední Evropa (letní èas)
