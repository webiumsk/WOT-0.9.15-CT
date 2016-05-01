# 2016.05.01 15:22:44 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortSettingsDayoffPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortSettingsDayoffPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

    def onApply(self, dayOff):
        """
        :param dayOff:
        :return :
        """
        self._printOverrideError('onApply')

    def as_setDescriptionsTextS(self, descriptionText, dayOffText):
        """
        :param descriptionText:
        :param dayOffText:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDescriptionsText(descriptionText, dayOffText)

    def as_setButtonsTextS(self, applyButtonText, cancelButtonText):
        """
        :param applyButtonText:
        :param cancelButtonText:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonsText(applyButtonText, cancelButtonText)

    def as_setButtonsTooltipsS(self, enabledApplyButtonTooltip, disabledApplyButtonTooltip):
        """
        :param enabledApplyButtonTooltip:
        :param disabledApplyButtonTooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonsTooltips(enabledApplyButtonTooltip, disabledApplyButtonTooltip)

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortsettingsdayoffpopovermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:44 Støední Evropa (letní èas)
