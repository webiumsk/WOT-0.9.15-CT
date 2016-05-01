# 2016.05.01 15:22:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IntroPageMeta.py
from gui.Scaleform.framework.entities.View import View

class IntroPageMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def stopVideo(self):
        """
        :return :
        """
        self._printOverrideError('stopVideo')

    def handleError(self, data):
        """
        :param data:
        :return :
        """
        self._printOverrideError('handleError')

    def as_playVideoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_playVideo(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\intropagemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:45 Støední Evropa (letní èas)
