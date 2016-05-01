# 2016.05.01 15:22:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AbstractRallyWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class AbstractRallyWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def canGoBack(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canGoBack')

    def onBrowseRallies(self):
        """
        :return :
        """
        self._printOverrideError('onBrowseRallies')

    def onBrowseStaticsRallies(self):
        """
        :return :
        """
        self._printOverrideError('onBrowseStaticsRallies')

    def onCreateRally(self):
        """
        :return :
        """
        self._printOverrideError('onCreateRally')

    def onJoinRally(self, rallyId, slotIndex, peripheryId):
        """
        :param rallyId:
        :param slotIndex:
        :param peripheryId:
        :return :
        """
        self._printOverrideError('onJoinRally')

    def as_loadViewS(self, flashAlias, pyAlias):
        """
        :param flashAlias:
        :param pyAlias:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(flashAlias, pyAlias)

    def as_enableWndCloseBtnS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enableWndCloseBtn(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\abstractrallywindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:35 Støední Evropa (letní èas)
