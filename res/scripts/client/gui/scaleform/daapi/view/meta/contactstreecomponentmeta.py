# 2016.05.01 15:22:39 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ContactsTreeComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContactsTreeComponentMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onGroupSelected(self, mainGroup, groupData):
        """
        :param mainGroup:
        :param groupData:
        :return :
        """
        self._printOverrideError('onGroupSelected')

    def searchLocalContact(self, flt):
        """
        :param flt:
        :return :
        """
        self._printOverrideError('searchLocalContact')

    def hasDisplayingContacts(self):
        """
        :return Boolean:
        """
        self._printOverrideError('hasDisplayingContacts')

    def as_updateInfoMessageS(self, enableSearchInput, title, message, warn):
        """
        :param enableSearchInput:
        :param title:
        :param message:
        :param warn:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateInfoMessage(enableSearchInput, title, message, warn)

    def as_getMainDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getMainDP()

    def as_setInitDataS(self, val):
        """
        :param val:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(val)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\contactstreecomponentmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:39 Støední Evropa (letní èas)
