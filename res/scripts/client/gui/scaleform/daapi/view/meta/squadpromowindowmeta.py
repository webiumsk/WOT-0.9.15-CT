# 2016.05.01 15:22:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SquadPromoWindowMeta.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta

class SquadPromoWindowMeta(SimpleWindowMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleWindowMeta
    null
    """

    def onHyperlinkClick(self):
        """
        :return :
        """
        self._printOverrideError('onHyperlinkClick')

    def as_setHyperlinkS(self, label):
        """
        :param label:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHyperlink(label)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\squadpromowindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:51 Støední Evropa (letní èas)
