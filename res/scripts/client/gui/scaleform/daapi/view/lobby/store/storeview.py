# 2016.05.01 15:22:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/store/StoreView.py
from account_helpers import AccountSettings
from account_helpers.AccountSettings import STORE_TAB
from gui.Scaleform.daapi.view.meta.StoreViewMeta import StoreViewMeta
from gui.Scaleform.locale.MENU import MENU
from gui.shared import events, EVENT_BUS_SCOPE
from gui.sounds.ambients import ShopEnv
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from shared_utils import findFirst
_TABS = ({'id': STORE_CONSTANTS.SHOP,
  'label': MENU.STORETAB_SHOP,
  'linkage': STORE_CONSTANTS.SHOP_LINKAGE}, {'id': STORE_CONSTANTS.INVENTORY,
  'label': MENU.STORETAB_INVENTORY,
  'linkage': STORE_CONSTANTS.INVENTORY_LINKAGE})

class StoreView(StoreViewMeta):
    __sound_env__ = ShopEnv

    def __init__(self, ctx = None):
        super(StoreView, self).__init__(ctx)
        self.__currentTab = AccountSettings.getFilter(STORE_TAB)

    def _populate(self):
        super(StoreView, self)._populate()
        self.as_initS({'currentViewIdx': self.__currentTab,
         'buttonBarData': _TABS})

    def onTabChange(self, tabId):
        index, _ = findFirst(lambda (i, e): e['id'] == tabId, enumerate(_TABS), (0, None))
        self.__currentTab = index
        return None

    def onClose(self):
        self.fireEvent(events.LoadViewEvent(VIEW_ALIAS.LOBBY_HANGAR), scope=EVENT_BUS_SCOPE.LOBBY)

    def _dispose(self):
        AccountSettings.setFilter(STORE_TAB, self.__currentTab)
        super(StoreView, self)._dispose()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\store\storeview.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:26 St�edn� Evropa (letn� �as)
