# 2016.05.01 15:21:31 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/boosters/BoostersWindow.py
from collections import defaultdict
from operator import attrgetter
from account_helpers.AccountSettings import AccountSettings, BOOSTERS_FILTER
from adisp import process
import constants
from goodies.goodie_constants import GOODIE_RESOURCE_TYPE
from gui.Scaleform.daapi.view.lobby.server_events import events_helpers
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from helpers.i18n import makeString as _ms
from gui import SystemMessages, makeHtmlString
from gui import DialogsInterface
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.boosters.BoostersPanelComponent import ADD_BOOSTER_ID
from gui.Scaleform.daapi.view.meta.BoostersWindowMeta import BoostersWindowMeta
from gui.goodies.Booster import MAX_ACTIVE_BOOSTERS_COUNT, BOOSTER_QUALITY_NAMES, BOOSTERS_ORDERS
from gui.goodies import g_goodiesCache
from gui.server_events import g_eventsCache, events_dispatcher as quests_events
from gui.shared.formatters import text_styles
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared.gui_items.processors.goodies import BoosterActivator
from gui.shared.utils import decorators
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from gui.shared.utils.functions import makeTooltip
from gui.Scaleform.genConsts.BOOSTER_CONSTANTS import BOOSTER_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID
from shared_utils import BitmaskHelper

class FILTER_STATE(BitmaskHelper):
    ALL = 0
    SMALL = 1
    MEDIUM = 2
    BIG = 4
    XP = 8
    CREW_XP = 16
    FREE_XP = 32
    CREDITS = 64
    BOOSTER_QUALITIES = ((SMALL, BOOSTER_QUALITY_NAMES.SMALL), (MEDIUM, BOOSTER_QUALITY_NAMES.MEDIUM), (BIG, BOOSTER_QUALITY_NAMES.BIG))
    BOOSTER_TYPES = ((XP, GOODIE_RESOURCE_TYPE.XP),
     (CREW_XP, GOODIE_RESOURCE_TYPE.CREW_XP),
     (FREE_XP, GOODIE_RESOURCE_TYPE.FREE_XP),
     (CREDITS, GOODIE_RESOURCE_TYPE.CREDITS))


class BoostersWindow(BoostersWindowMeta):

    def __init__(self, ctx = None):
        super(BoostersWindow, self).__init__()
        self.__availableBoosters = None
        self.__boosterQuests = None
        self.__activeBoosters = None
        self.__isReceivedBoostersTab = ctx.get('slotID', None) != ADD_BOOSTER_ID
        self.__boostersInQuestCount = 0
        self.__qualities = []
        self.__boosterTypes = []
        self.__questsDescriptor = events_helpers.getTutorialEventsDescriptor()
        return

    def onWindowClose(self):
        self.destroy()

    def requestBoostersArray(self, isReceivedBoostersTab):
        self.__isReceivedBoostersTab = isReceivedBoostersTab
        self.as_setListDataS(self.__getBoostersVOs(), False)
        self.__setCommonData()

    @process
    def onBoosterActionBtnClick(self, boosterID, questID):
        if self.__isReceivedBoostersTab:
            booster = g_goodiesCache.getBooster(boosterID)
            activeBooster = self.__getActiveBoosterByType(booster.boosterType)
            if activeBooster is not None:
                canActivate = yield DialogsInterface.showDialog(I18nConfirmDialogMeta(BOOSTER_CONSTANTS.BOOSTER_ACTIVATION_CONFORMATION_TEXT_KEY, messageCtx={'newBoosterName': text_styles.middleTitle(booster.description),
                 'curBoosterName': text_styles.middleTitle(activeBooster.description)}, focusedID=DIALOG_BUTTON_ID.CLOSE))
            else:
                canActivate = True
            if canActivate:
                self.__activateBoosterRequest(booster)
        else:
            if questID and questID.isdigit():
                questID = int(questID)
            quest = g_eventsCache.getAllQuests(includePotapovQuests=True).get(questID)
            if quest is not None:
                quests_events.showEventsWindow(quest.getID(), quest.getType())
            elif self.__questsDescriptor and self.__questsDescriptor.getChapter(questID):
                quests_events.showEventsWindow(questID, constants.EVENT_TYPE.TUTORIAL)
        return

    def onFiltersChange(self, filters):
        self.__setFilters(filters)
        self.__update()

    def onResetFilters(self):
        self.__setFilters(FILTER_STATE.ALL)
        self.__update(FILTER_STATE.ALL)

    def _populate(self):
        super(BoostersWindow, self)._populate()
        self.__setFilters(AccountSettings.getFilter(BOOSTERS_FILTER))
        g_clientUpdateManager.addCallbacks({'goodies': self.__onUpdateBoosters})
        g_eventsCache.onSyncCompleted += self.__onQuestsUpdate
        self.__boosterQuests = self.__getBoosterQuests()
        self.__activeBoosters = self.__getActiveBoosters()
        self.__update()
        self.__setStaticData()

    def _dispose(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        g_eventsCache.onSyncCompleted -= self.__onQuestsUpdate
        self.__availableBoosters = None
        self.__boosterQuests = None
        self.__activeBoosters = None
        self.__isReceivedBoostersTab = None
        self.__qualities = None
        self.__boosterTypes = None
        self.__questsDescriptor = None
        super(BoostersWindow, self)._dispose()
        return

    def __onQuestsUpdate(self, *args):
        self.__boosterQuests = self.__getBoosterQuests()
        self.__update()

    def __onUpdateBoosters(self, *args):
        self.__activeBoosters = self.__getActiveBoosters()
        self.__update()

    def __update(self, filterState = -1):
        self.__availableBoosters = self.__getAvailableBoosters()
        self.__boostersInQuestCount = sum((count for _, _, _, count in self.__qBoostersIterator(checkFilters=True)))
        self.__setCommonData(filterState)
        self.as_setListDataS(self.__getBoostersVOs(), False)

    def __setStaticData(self):
        self.as_setStaticDataS({'windowTitle': _ms(MENU.BOOSTERSWINDOW_TITLE),
         'closeBtnLabel': _ms(MENU.BOOSTERSWINDOW_CLOSEBTN_LABEL),
         'noInfoBgSource': RES_ICONS.MAPS_ICONS_BOOSTERS_NOINFOBG,
         'filtersData': {'qualityFiltersLabel': text_styles.main(MENU.BOOSTERSWINDOW_LEVELFILTERS_LABEL),
                         'typeFiltersLabel': text_styles.main(MENU.BOOSTERSWINDOW_TYPEFILTERS_LABEL),
                         'qualityFilters': self.__packFiltersData(self.__packQualityFiltersItems()),
                         'typeFilters': self.__packFiltersData(self.__packTypeFiltersItems())}})

    def ___packNoInfo(self):
        if self.__isReceivedBoostersTab and self.__getAvailableTotal() > 0 or not self.__isReceivedBoostersTab and self.__getNotAvailableTotal() > 0:
            title = text_styles.middleTitle(MENU.BOOSTERSWINDOW_BOOSTERSTABLE_NOINFO_NOTFOUND_TITLE)
            message = text_styles.main(MENU.BOOSTERSWINDOW_BOOSTERSTABLE_NOINFO_NOTFOUND_MESSAGE)
            returnBtnLabel = _ms(MENU.BOOSTERSWINDOW_RETURNBTN_LABEL)
        else:
            title = ''
            message = makeHtmlString('html_templates:lobby/textStyle', 'alignText', {'align': 'center',
             'message': text_styles.standard(MENU.BOOSTERSWINDOW_BOOSTERSTABLE_NOINFO_EMPTY_MESSAGE)})
            returnBtnLabel = ''
        return {'title': title,
         'message': message,
         'returnBtnLabel': returnBtnLabel}

    def __packFiltersData(self, items):
        return {'items': items,
         'minSelectedItems': 0}

    def __packFilterItem(self, icon, value, tooltip, selected):
        return {'icon': icon,
         'filterValue': value,
         'selected': selected,
         'tooltip': makeTooltip(None, _ms(tooltip))}

    def __packQualityFiltersItems(self):
        return [self.__packFilterItem(RES_ICONS.MAPS_ICONS_FILTERS_LEVELS_LEVEL_1, FILTER_STATE.SMALL, TOOLTIPS.BOOSTER_FILTERS_QUALITYSMALL_BODY, BOOSTER_QUALITY_NAMES.SMALL in self.__qualities), self.__packFilterItem(RES_ICONS.MAPS_ICONS_FILTERS_LEVELS_LEVEL_2, FILTER_STATE.MEDIUM, TOOLTIPS.BOOSTER_FILTERS_QUALITYMEDIUM_BODY, BOOSTER_QUALITY_NAMES.MEDIUM in self.__qualities), self.__packFilterItem(RES_ICONS.MAPS_ICONS_FILTERS_LEVELS_LEVEL_3, FILTER_STATE.BIG, TOOLTIPS.BOOSTER_FILTERS_QUALITYBIG_BODY, BOOSTER_QUALITY_NAMES.BIG in self.__qualities)]

    def __packTypeFiltersItems(self):
        return [self.__packFilterItem(RES_ICONS.MAPS_ICONS_BOOSTERS_BOOSTER_XP_SMALL_BW, FILTER_STATE.XP, TOOLTIPS.BOOSTER_FILTERS_TYPEXP_BODY, GOODIE_RESOURCE_TYPE.XP in self.__boosterTypes),
         self.__packFilterItem(RES_ICONS.MAPS_ICONS_BOOSTERS_BOOSTER_CREW_XP_SMALL_BW, FILTER_STATE.CREW_XP, TOOLTIPS.BOOSTER_FILTERS_TYPECREWXP_BODY, GOODIE_RESOURCE_TYPE.CREW_XP in self.__boosterTypes),
         self.__packFilterItem(RES_ICONS.MAPS_ICONS_BOOSTERS_BOOSTER_FREE_XP_SMALL_BW, FILTER_STATE.FREE_XP, TOOLTIPS.BOOSTER_FILTERS_TYPEFREEXP_BODY, GOODIE_RESOURCE_TYPE.FREE_XP in self.__boosterTypes),
         self.__packFilterItem(RES_ICONS.MAPS_ICONS_BOOSTERS_BOOSTER_CREDITS_SMALL_BW, FILTER_STATE.CREDITS, TOOLTIPS.BOOSTER_FILTERS_TYPECREDITS_BODY, GOODIE_RESOURCE_TYPE.CREDITS in self.__boosterTypes)]

    def __setCommonData(self, filterState = -1):
        isHaveNotInfo = not self.__boostersInQuestCount or self.__getNotAvailableTotal() == 0
        if self.__isReceivedBoostersTab:
            isHaveNotInfo = not len(self.__availableBoosters) or self.__getAvailableTotal() == 0
        self.as_setDataS({'isHaveNotInfo': isHaveNotInfo,
         'noInfoData': self.___packNoInfo(),
         'availableTabLabel': self.__getAvailableTabLabel(),
         'notAvailableTabLabel': self.__getNotAvailableTabLabel(),
         'activeText': self.__getActiveText(),
         'isReceivedBoostersTab': self.__isReceivedBoostersTab,
         'filterState': filterState})

    def __getAvailableTabLabel(self):
        boostersCount = sum((booster.count for booster in self.__availableBoosters))
        return _ms(MENU.BOOSTERSWINDOW_TABS_AVAILABLELABEL, availableNo=boostersCount, totalNo=str(self.__getAvailableTotal()))

    def __getNotAvailableTabLabel(self):
        return _ms(MENU.BOOSTERSWINDOW_TABS_NOTAVAILABLELABEL, notAvailableNo=self.__boostersInQuestCount, totalNo=str(self.__getNotAvailableTotal()))

    def __getActiveText(self):
        return text_styles.highTitle(_ms(MENU.BOOSTERSWINDOW_ACTIVEBOOSTERS, activeNo=len(self.__activeBoosters), allNo=MAX_ACTIVE_BOOSTERS_COUNT))

    def __getBoostersVOs(self):
        boosterVOs = []
        if self.__isReceivedBoostersTab:
            for booster in self.__availableBoosters:
                boosterVOs.append(self.__makeBoosterVO(booster, booster.isReadyToActivate))

        else:
            qBoosters = [ boosterInfo for boosterInfo in self.__qBoostersIterator(checkFilters=True) ]
            for questID, qUserName, booster, count in sorted(qBoosters, self._sortQuestsBoosters):
                boosterVOs.append(self.__makeBoosterVO(booster, questID is not None, questID, qUserName, count))

        return boosterVOs

    @classmethod
    def _sortQuestsBoosters(cls, a, b):
        booster1 = a[2]
        booster2 = b[2]
        return cls._sortAvailableBoosters(booster1, booster2)

    def __qBoostersIterator(self, checkFilters = True):
        for (questID, qUserName), boosters in self.__boosterQuests.iteritems():
            for booster, count in boosters:
                if checkFilters:
                    if self.__isBoosterValid(booster):
                        yield (questID,
                         qUserName,
                         booster,
                         count)
                else:
                    yield count

    def __getBoosterFullName(self, booster):
        return text_styles.middleTitle(booster.fullUserName)

    def __makeBoosterVO(self, booster, isBtnEnabled, questID = None, qUserName = None, qBoosterCount = None):
        activateBtnLabel = MENU.BOOSTERSWINDOW_BOOSTERSTABLERENDERER_ACTIVATEBTNLABEL if questID is None else MENU.BOOSTERSWINDOW_BOOSTERSTABLERENDERER_GOTOQUESTBTNLABEL
        return {'id': booster.boosterID,
         'questID': str(questID) if questID else None,
         'actionBtnEnabled': isBtnEnabled,
         'actionBtnTooltip': self.__getQuestTooltip(qUserName, isBtnEnabled),
         'headerText': self.__getBoosterFullName(booster),
         'descriptionText': text_styles.main(booster.description),
         'addDescriptionText': self.__getAdditionalDescription(booster, qUserName),
         'actionBtnLabel': _ms(activateBtnLabel),
         'tooltip': TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO,
         'boosterSlotVO': self.__makeBoosterSlotVO(booster, qBoosterCount)}

    def __makeBoosterSlotVO(self, booster, qBoosterCount):
        boosterCount = qBoosterCount or booster.count
        return {'boosterId': booster.boosterID,
         'icon': booster.icon,
         'countText': text_styles.counter(str(boosterCount)),
         'showCount': boosterCount > 1,
         'qualityIconSrc': booster.getQualityIcon(),
         'slotLinkage': BOOSTER_CONSTANTS.SLOT_UI,
         'showLeftTime': False}

    def __getQuestTooltip(self, qUserName, isBtnEnabled):
        if qUserName is not None:
            return makeTooltip(None, _ms(TOOLTIPS.BOOSTER_QUESTLINKBTN_BODY, questName=qUserName))
        elif not isBtnEnabled:
            return makeTooltip(None, _ms(TOOLTIPS.BOOSTER_ACTIVEBTN_DISABLED_BODY))
        else:
            return ''

    def __getAdditionalDescription(self, booster, qUserName):
        if qUserName is not None:
            text = _ms(MENU.BOOSTERSWINDOW_BOOSTERSTABLERENDERER_QUESTFOROPEN, questName=qUserName)
        elif booster.expiryTime:
            text = _ms(MENU.BOOSTERSWINDOW_BOOSTERSTABLERENDERER_TIME, tillTime=booster.getExpiryDate())
        else:
            text = _ms(MENU.BOOSTERSWINDOW_BOOSTERSTABLERENDERER_UNDEFINETIME)
        return text_styles.standard(text)

    def __getAvailableBoosters(self):
        criteria = REQ_CRITERIA.BOOSTER.IN_ACCOUNT | REQ_CRITERIA.CUSTOM(self.__isBoosterValid)
        return sorted(g_goodiesCache.getBoosters(criteria=criteria).values(), self._sortAvailableBoosters)

    def __getAvailableTotal(self):
        boosters = g_goodiesCache.getBoosters(criteria=REQ_CRITERIA.BOOSTER.IN_ACCOUNT).values()
        return sum((booster.count for booster in boosters))

    def __getNotAvailableTotal(self):
        return sum(self.__qBoostersIterator(checkFilters=False))

    @classmethod
    def _sortAvailableBoosters(cls, a, b):
        return cmp(a.quality, b.quality) or cmp(BOOSTERS_ORDERS[a.boosterType], BOOSTERS_ORDERS[b.boosterType]) or cmp(b.effectValue, a.effectValue)

    def __getActiveBoosters(self):
        return g_goodiesCache.getBoosters(criteria=REQ_CRITERIA.BOOSTER.ACTIVE).values()

    def __getActiveBoosterByType(self, bType):
        criteria = REQ_CRITERIA.BOOSTER.ACTIVE | REQ_CRITERIA.BOOSTER.BOOSTER_TYPES([bType])
        activeBoosters = g_goodiesCache.getBoosters(criteria=criteria).values()
        if len(activeBoosters) > 0:
            return max(activeBoosters, key=attrgetter('effectValue'))
        else:
            return None

    def __getBoosterQuests(self):
        result = defaultdict(list)
        quests = events_helpers.getBoosterQuests()
        for q in quests.itervalues():
            bonuses = q.getBonuses('goodies')
            for b in bonuses:
                boosters = b.getBoosters()
                for booster, count in boosters.iteritems():
                    result[q.getID(), q.getUserName()].append((booster, count))

        for chapter, boosters in events_helpers.getTutorialQuestsBoosters().iteritems():
            result[chapter.getID(), chapter.getTitle()].extend(boosters)

        return result

    @decorators.process('loadStats')
    def __activateBoosterRequest(self, booster):
        result = yield BoosterActivator(booster).request()
        if len(result.userMsg):
            SystemMessages.g_instance.pushI18nMessage(result.userMsg, type=result.sysMsgType)

    def __setFilters(self, filterState):
        self.__qualities = []
        self.__boosterTypes = []
        for quality, param in FILTER_STATE.BOOSTER_QUALITIES:
            if filterState & quality:
                self.__qualities.append(param)

        for bType, param in FILTER_STATE.BOOSTER_TYPES:
            if filterState & bType:
                self.__boosterTypes.append(param)

        AccountSettings.setFilter(BOOSTERS_FILTER, filterState)

    def __isBoosterValid(self, booster):
        isTypeValid = True
        if len(self.__boosterTypes):
            isTypeValid = booster.boosterType in self.__boosterTypes
        isQualityValid = True
        if len(self.__qualities):
            isQualityValid = booster.quality in self.__qualities
        return isTypeValid and isQualityValid
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\boosters\boosterswindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:21:31 St�edn� Evropa (letn� �as)
