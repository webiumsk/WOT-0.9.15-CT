# 2016.05.01 15:22:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LegalInfoWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class LegalInfoWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def getLegalInfo(self):
        """
        :return :
        """
        self._printOverrideError('getLegalInfo')

    def onCancelClick(self):
        """
        :return :
        """
        self._printOverrideError('onCancelClick')

    def as_setLegalInfoS(self, legalInfo):
        """
        :param legalInfo:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setLegalInfo(legalInfo)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\legalinfowindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:46 Støední Evropa (letní èas)
