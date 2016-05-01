# 2016.05.01 15:24:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/BaseManageContactViewMeta.py
from messenger.gui.Scaleform.view.BaseContactView import BaseContactView

class BaseManageContactViewMeta(BaseContactView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseContactView
    null
    """

    def checkText(self, txt):
        """
        :param txt:
        :return :
        """
        self._printOverrideError('checkText')

    def as_setLabelS(self, msg):
        """
        :param msg:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setLabel(msg)

    def as_setInputTextS(self, msg):
        """
        :param msg:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInputText(msg)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\basemanagecontactviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:56 Støední Evropa (letní èas)
