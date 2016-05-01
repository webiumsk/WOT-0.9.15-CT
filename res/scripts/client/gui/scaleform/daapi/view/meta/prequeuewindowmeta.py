# 2016.05.01 15:22:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrequeueWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class PrequeueWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def requestToEnqueue(self):
        """
        :return :
        """
        self._printOverrideError('requestToEnqueue')

    def requestToLeave(self):
        """
        :return :
        """
        self._printOverrideError('requestToLeave')

    def showFAQWindow(self):
        """
        :return :
        """
        self._printOverrideError('showFAQWindow')

    def isEnqueueBtnEnabled(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isEnqueueBtnEnabled')

    def isLeaveBtnEnabled(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isLeaveBtnEnabled')

    def as_enableLeaveBtnS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enableLeaveBtn(value)

    def as_enableEnqueueBtnS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enableEnqueueBtn(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\prequeuewindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:47 Støední Evropa (letní èas)
