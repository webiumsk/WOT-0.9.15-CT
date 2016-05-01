# 2016.05.01 15:22:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LoginQueueWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class LoginQueueWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onCancelClick(self):
        """
        :return :
        """
        self._printOverrideError('onCancelClick')

    def onAutoLoginClick(self):
        """
        :return :
        """
        self._printOverrideError('onAutoLoginClick')

    def as_setTitleS(self, title):
        """
        :param title:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(title)

    def as_setMessageS(self, message):
        """
        :param message:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMessage(message)

    def as_setCancelLabelS(self, cancelLabel):
        """
        :param cancelLabel:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCancelLabel(cancelLabel)

    def as_showAutoLoginBtnS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showAutoLoginBtn(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\loginqueuewindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:46 Støední Evropa (letní èas)
