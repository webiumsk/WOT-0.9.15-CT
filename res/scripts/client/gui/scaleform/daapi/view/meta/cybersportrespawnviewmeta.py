# 2016.05.01 15:22:40 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportRespawnViewMeta.py
from gui.Scaleform.framework.entities.View import View

class CyberSportRespawnViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def as_setMapBGS(self, imgsource):
        """
        :param imgsource:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMapBG(imgsource)

    def as_changeAutoSearchStateS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchState(value)

    def as_hideAutoSearchS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideAutoSearch()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\cybersportrespawnviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:40 Støední Evropa (letní èas)
