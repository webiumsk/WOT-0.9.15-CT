# 2016.05.01 15:22:38 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanSearchWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ClanSearchWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def search(self, text):
        """
        :param text:
        :return :
        """
        self._printOverrideError('search')

    def previousPage(self):
        """
        :return :
        """
        self._printOverrideError('previousPage')

    def nextPage(self):
        """
        :return :
        """
        self._printOverrideError('nextPage')

    def dummyButtonPress(self):
        """
        :return :
        """
        self._printOverrideError('dummyButtonPress')

    def as_getDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setStateDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStateData(data)

    def as_setDummyS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDummy(data)

    def as_setDummyVisibleS(self, visible):
        """
        :param visible:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDummyVisible(visible)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\clansearchwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:39 Støední Evropa (letní èas)
