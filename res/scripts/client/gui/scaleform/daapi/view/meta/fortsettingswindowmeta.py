# 2016.05.01 15:22:44 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortSettingsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortSettingsWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def activateDefencePeriod(self):
        """
        :return :
        """
        self._printOverrideError('activateDefencePeriod')

    def disableDefencePeriod(self):
        """
        :return :
        """
        self._printOverrideError('disableDefencePeriod')

    def cancelDisableDefencePeriod(self):
        """
        :return :
        """
        self._printOverrideError('cancelDisableDefencePeriod')

    def as_setFortClanInfoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFortClanInfo(data)

    def as_setMainStatusS(self, title, msg, toolTip):
        """
        :param title:
        :param msg:
        :param toolTip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMainStatus(title, msg, toolTip)

    def as_setViewS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setView(value)

    def as_setDataForActivatedS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDataForActivated(data)

    def as_setCanDisableDefencePeriodS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCanDisableDefencePeriod(value)

    def as_setDataForNotActivatedS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDataForNotActivated(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortsettingswindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:44 Støední Evropa (letní èas)
