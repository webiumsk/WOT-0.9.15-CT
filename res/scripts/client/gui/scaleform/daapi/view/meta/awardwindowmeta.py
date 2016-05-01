# 2016.05.01 15:22:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AwardWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class AwardWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onOKClick(self):
        """
        :return :
        """
        self._printOverrideError('onOKClick')

    def onTakeNextClick(self):
        """
        :return :
        """
        self._printOverrideError('onTakeNextClick')

    def onCloseClick(self):
        """
        :return :
        """
        self._printOverrideError('onCloseClick')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\awardwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:35 Støední Evropa (letní èas)
