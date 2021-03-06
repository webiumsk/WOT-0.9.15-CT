# 2016.05.01 15:21:24 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/FalloutBattleSelectorWindow.py
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.game_control import getFalloutCtrl
from gui.prb_control.context import PrebattleAction
from gui.prb_control.prb_helpers import GlobalListener
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from gui.Scaleform.daapi.view.meta.FalloutBattleSelectorWindowMeta import FalloutBattleSelectorWindowMeta
from gui.Scaleform.locale.FALLOUT import FALLOUT
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.formatters.text_styles import promoSubTitle, main
from gui.shared.utils.functions import makeTooltip
from messenger.ext import channel_num_gen
from messenger.ext.channel_num_gen import SPECIAL_CLIENT_WINDOWS

class FalloutBattleSelectorWindow(FalloutBattleSelectorWindowMeta, GlobalListener):

    def __init__(self, ctx = None):
        super(FalloutBattleSelectorWindow, self).__init__(ctx)
        self.__falloutCtrl = None
        return

    def onSelectCheckBoxAutoSquad(self, isSelected):
        self.__falloutCtrl.setAutomatch(isSelected)

    def onWindowMinimize(self):
        self.destroy()

    def onWindowClose(self):
        self.destroy()
        if not self.prbDispatcher.getFunctionalState().hasLockedState:
            self.prbDispatcher.doSelectAction(PrebattleAction(PREBATTLE_ACTION_NAME.RANDOM_QUEUE))

    def onDominationBtnClick(self):
        self.prbDispatcher.doSelectAction(PrebattleAction(PREBATTLE_ACTION_NAME.FALLOUT_CLASSIC))
        self.destroy()

    def onMultiteamBtnClick(self):
        self.prbDispatcher.doSelectAction(PrebattleAction(PREBATTLE_ACTION_NAME.FALLOUT_MULTITEAM))
        self.destroy()

    def onEnqueued(self, queueType, *args):
        self.as_setBtnStatesS(self.__getBtnsStateData(False))
        self._onBtnsDisableStateChanged()

    def onDequeued(self, queueType, *args):
        self.as_setBtnStatesS(self.__getBtnsStateData(True))
        self._onBtnsDisableStateChanged()

    def onUnitFlagsChanged(self, flags, timeLeft):
        if self.unitFunctional.hasLockedState():
            if flags.isInSearch() or flags.isInQueue() or flags.isInArena():
                self.as_setBtnStatesS(self.__getBtnsStateData(False))
        else:
            self.as_setBtnStatesS(self.__getBtnsStateData(True))
        self._onBtnsDisableStateChanged()

    def getClientID(self):
        return channel_num_gen.getClientID4SpecialWindow(SPECIAL_CLIENT_WINDOWS.FALLOUT)

    def _populate(self):
        super(FalloutBattleSelectorWindow, self)._populate()
        self.startGlobalListening()
        self.__falloutCtrl = getFalloutCtrl()
        self.__falloutCtrl.onSettingsChanged += self.__updateFalloutSettings
        self.__falloutCtrl.onAutomatchChanged += self.__updateFalloutSettings
        self.__updateFalloutSettings()
        if self.prbDispatcher.getFunctionalState().hasLockedState or not self.__falloutCtrl.canChangeBattleType():
            self.as_setBtnStatesS(self.__getBtnsStateData(False))

    def _dispose(self):
        self.stopGlobalListening()
        if self.__falloutCtrl:
            self.__falloutCtrl.onSettingsChanged -= self.__updateFalloutSettings
            self.__falloutCtrl.onAutomatchChanged -= self.__updateFalloutSettings
        self.__falloutCtrl = None
        super(FalloutBattleSelectorWindow, self)._dispose()
        return

    def _getTooltipData(self):
        data = {'autoSquadStr': makeTooltip(TOOLTIPS.FALLOUTBATTLESELECTORWINDOW_INFO_HEADER, TOOLTIPS.FALLOUTBATTLESELECTORWINDOW_INFO_BODY, attention=TOOLTIPS.FALLOUTBATTLESELECTORWINDOW_INFO_ALERT)}
        data['dominationStr'] = TOOLTIPS.BATTLESELECTORWINDOW_TOOLTIP_DOMINATION_SELECTBTN
        data['multiteamStr'] = TOOLTIPS.BATTLESELECTORWINDOW_TOOLTIP_MULTITEAM_SELECTBTN
        if self.prbDispatcher.getFunctionalState().hasLockedState:
            data['dominationStr'] = TOOLTIPS.FALLOUTBATTLESELECTORWINDOW_BTNDISABLED
            data['multiteamStr'] = TOOLTIPS.FALLOUTBATTLESELECTORWINDOW_BTNDISABLED
        elif not self.__falloutCtrl.canChangeBattleType():
            data['dominationStr'] = TOOLTIPS.FALLOUTBATTLESELECTORWINDOW_BTNINSQUADDISABLED
            data['multiteamStr'] = TOOLTIPS.FALLOUTBATTLESELECTORWINDOW_BTNINSQUADDISABLED
        return data

    def _onBtnsDisableStateChanged(self):
        self.as_setTooltipsS(self._getTooltipData())

    def __getBtnsStateData(self, isEnabled):
        return {'dominationBtnEnabled': isEnabled,
         'multiteamBtnEnabled': isEnabled,
         'closeBtnEnabled': isEnabled,
         'autoSquadCheckboxEnabled': isEnabled}

    def __updateFalloutSettings(self):
        if not self.__falloutCtrl.isEnabled():
            return self.onWindowClose()
        self.as_setInitDataS({'windowTitle': FALLOUT.BATTLESELECTORWINDOW_TITLE,
         'headerTitleStr': promoSubTitle(FALLOUT.BATTLESELECTORWINDOW_HEADERTITLESTR),
         'headerDescStr': main(FALLOUT.BATTLESELECTORWINDOW_HEADERDESC),
         'dominationBattleTitleStr': promoSubTitle(FALLOUT.BATTLESELECTORWINDOW_DOMINATION_TITLE),
         'dominationBattleDescStr': main(FALLOUT.BATTLESELECTORWINDOW_DOMINATION_DESCR),
         'dominationBattleBtnStr': FALLOUT.BATTLESELECTORWINDOW_DOMINATIONBATTLEBTNLBL,
         'multiteamTitleStr': promoSubTitle(FALLOUT.BATTLESELECTORWINDOW_MULTITEAM_TITLE),
         'multiteamDescStr': main(FALLOUT.BATTLESELECTORWINDOW_MULTITEAM_DESCR),
         'multiteamBattleBtnStr': FALLOUT.BATTLESELECTORWINDOW_MULTITEAMBATTLEBTNLBL,
         'bgImg': RES_ICONS.MAPS_ICONS_LOBBY_FALLOUTBATTLESELECTORBG,
         'multiteamAutoSquadEnabled': self.__falloutCtrl.isAutomatch(),
         'multiteamAutoSquadLabel': FALLOUT.FALLOUTBATTLESELECTORWINDOW_AUTOSQUAD_LABEL,
         'tooltipData': self._getTooltipData()})
        if self.prbDispatcher.getFunctionalState().hasLockedState or not self.__falloutCtrl.canChangeBattleType():
            self.as_setBtnStatesS(self.__getBtnsStateData(False))
        else:
            self.as_setBtnStatesS(self.__getBtnsStateData(True))
        self._onBtnsDisableStateChanged()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\falloutbattleselectorwindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:21:25 St�edn� Evropa (letn� �as)
