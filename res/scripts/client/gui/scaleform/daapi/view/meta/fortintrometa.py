# 2016.05.01 15:22:43 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortIntroMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyIntroView import BaseRallyIntroView

class FortIntroMeta(BaseRallyIntroView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyIntroView
    null
    """

    def as_setIntroDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setIntroData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortintrometa.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:43 Støední Evropa (letní èas)
