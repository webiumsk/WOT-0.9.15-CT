# 2016.05.01 15:24:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/FAQWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FAQWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onLinkClicked(self, name):
        """
        :param name:
        :return :
        """
        self._printOverrideError('onLinkClicked')

    def as_appendTextS(self, text):
        """
        :param text:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_appendText(text)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\faqwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:56 Støední Evropa (letní èas)
