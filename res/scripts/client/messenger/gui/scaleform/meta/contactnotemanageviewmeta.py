# 2016.05.01 15:24:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ContactNoteManageViewMeta.py
from messenger.gui.Scaleform.meta.BaseManageContactViewMeta import BaseManageContactViewMeta

class ContactNoteManageViewMeta(BaseManageContactViewMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseManageContactViewMeta
    null
    """

    def sendData(self, data):
        """
        :param data:
        :return :
        """
        self._printOverrideError('sendData')

    def as_setUserPropsS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setUserProps(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\contactnotemanageviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:56 Støední Evropa (letní èas)
