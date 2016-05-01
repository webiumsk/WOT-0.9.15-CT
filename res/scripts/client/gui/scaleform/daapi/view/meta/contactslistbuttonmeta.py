# 2016.05.01 15:22:39 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ContactsListButtonMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContactsListButtonMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setContactsCountS(self, num):
        """
        :param num:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setContactsCount(num)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\contactslistbuttonmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:39 Støední Evropa (letní èas)
