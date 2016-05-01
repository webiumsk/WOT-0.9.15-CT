# 2016.05.01 15:22:54 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WindowViewMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class WindowViewMeta(WrapperViewMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends WrapperViewMeta
    null
    """

    def onWindowMinimize(self):
        """
        :return :
        """
        self._printOverrideError('onWindowMinimize')

    def onSourceLoaded(self):
        """
        :return :
        """
        self._printOverrideError('onSourceLoaded')

    def onTryClosing(self):
        """
        :return Boolean:
        """
        self._printOverrideError('onTryClosing')

    def as_getGeometryS(self):
        """
        :return Array:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getGeometry()

    def as_setGeometryS(self, x, y, width, height):
        """
        :param x:
        :param y:
        :param width:
        :param height:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setGeometry(x, y, width, height)

    def as_isModalS(self):
        """
        :return Boolean:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_isModal()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\windowviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:54 Støední Evropa (letní èas)
