# 2016.05.01 15:24:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/SearchContactViewMeta.py
from messenger.gui.Scaleform.view.BaseContactView import BaseContactView

class SearchContactViewMeta(BaseContactView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseContactView
    null
    """

    def search(self, data):
        """
        :param data:
        :return :
        """
        self._printOverrideError('search')

    def as_getSearchDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()

    def as_setSearchResultTextS(self, message):
        """
        :param message:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchResultText(message)

    def as_setSearchDisabledS(self, coolDown):
        """
        :param coolDown:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchDisabled(coolDown)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\searchcontactviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:57 Støední Evropa (letní èas)
