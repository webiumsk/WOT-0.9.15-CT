# 2016.05.01 15:22:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SquadWindowMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyMainWindow import BaseRallyMainWindow

class SquadWindowMeta(BaseRallyMainWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyMainWindow
    null
    """

    def as_setComponentIdS(self, componentId):
        """
        :param componentId:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setComponentId(componentId)

    def as_setWindowTitleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\squadwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:51 Støední Evropa (letní èas)
