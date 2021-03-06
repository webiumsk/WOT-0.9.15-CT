# 2016.05.01 15:21:02 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/storage/fallout_storage.py
from UnitBase import INV_ID_CLEAR_VEHICLE
from account_helpers import AccountSettings
from account_helpers.AccountSettings import FALLOUT_VEHICLES
from account_helpers.settings_core import g_settingsCore
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
from constants import QUEUE_TYPE
from gui.prb_control.storage.local_storage import LocalStorage
from gui.server_events import g_eventsCache
from gui.shared import g_itemsCache
_SETTINGS_DEFAULTS = {'isEnabled': False,
 'isAutomatch': False,
 'falloutBattleType': QUEUE_TYPE.UNKNOWN,
 'hasVehicleLvl8': False,
 'hasVehicleLvl10': False}

class FalloutLocalStorage(LocalStorage):
    __slots__ = ('__settings', '__intCDs')

    def __init__(self):
        super(FalloutLocalStorage, self).__init__()
        self.__settings = {}
        self.__intCDs = {}

    def init(self):
        pass

    def fini(self):
        self.__settings.clear()
        self.__intCDs.clear()

    def swap(self):
        self.__settings = g_settingsCore.serverSettings.getSection(SETTINGS_SECTIONS.FALLOUT, _SETTINGS_DEFAULTS)
        self.__intCDs = AccountSettings.getFavorites(FALLOUT_VEHICLES)
        self.validateSelectedVehicles()

    def release(self, queueType = QUEUE_TYPE.UNKNOWN):
        self.__settings['isEnabled'] = True
        self.__settings['falloutBattleType'] = queueType
        g_settingsCore.serverSettings.setSection(SETTINGS_SECTIONS.FALLOUT, self.__settings)

    def suspend(self):
        self.__settings['isEnabled'] = False
        self.__settings['falloutBattleType'] = QUEUE_TYPE.UNKNOWN
        g_settingsCore.serverSettings.setSection(SETTINGS_SECTIONS.FALLOUT, self.__settings)

    def isEnabled(self):
        return g_eventsCache.isFalloutEnabled() and bool(self.__settings['isEnabled'])

    def getBattleType(self):
        return self.__settings['falloutBattleType']

    def setBattleType(self, value):
        raise value in QUEUE_TYPE.FALLOUT or AssertionError('Unsupported battle type {} given!'.format(value))
        self.__settings['falloutBattleType'] = value
        g_settingsCore.serverSettings.setSection(SETTINGS_SECTIONS.FALLOUT, self.__settings)

    def isAutomatch(self):
        return bool(self.__settings['isAutomatch'])

    def setAutomatch(self, isAutomatch):
        self.__settings['isAutomatch'] = isAutomatch
        g_settingsCore.serverSettings.setSection(SETTINGS_SECTIONS.FALLOUT, self.__settings)

    def getVehiclesInvIDs(self, excludeEmpty = False):
        vehiclesIntCDs = self.__intCDs.get(self.getBattleType(), ())
        vehiclesInvIDs = []
        for intCD in vehiclesIntCDs:
            vehicle = g_itemsCache.items.getItemByCD(intCD)
            if vehicle is None:
                if not excludeEmpty:
                    vehiclesInvIDs.append(INV_ID_CLEAR_VEHICLE)
            else:
                vehiclesInvIDs.append(vehicle.invID)

        return vehiclesInvIDs

    def setVehiclesInvIDs(self, vehicles):
        vehiclesIntCDs = []
        for invID in vehicles:
            vehicle = g_itemsCache.items.getVehicle(invID)
            if vehicle is None:
                vehiclesIntCDs.append(INV_ID_CLEAR_VEHICLE)
            else:
                vehiclesIntCDs.append(vehicle.intCD)

        self.__intCDs[self.getBattleType()] = vehiclesIntCDs
        AccountSettings.setFavorites(FALLOUT_VEHICLES, self.__intCDs)
        return

    def getSelectedVehicles(self):
        return filter(None, map(g_itemsCache.items.getItemByCD, self.__intCDs.get(self.getBattleType(), ())))

    def validateSelectedVehicles(self):
        config = self.getConfig()
        battleType = self.getBattleType()
        vehicles = self.__intCDs.get(battleType, ())
        if not config.hasRequiredVehicles():
            valid = ()
        else:
            maxVehs = config.maxVehiclesPerPlayer
            valid = [INV_ID_CLEAR_VEHICLE] * maxVehs
            vehGetter = g_itemsCache.items.getItemByCD
            for idx, intCD in enumerate(vehicles[:maxVehs]):
                invVehicle = vehGetter(intCD)
                if invVehicle is not None and invVehicle.isInInventory:
                    valid[idx] = intCD

        if valid != vehicles:
            self.__intCDs[battleType] = valid
            AccountSettings.setFavorites(FALLOUT_VEHICLES, self.__intCDs)
        return

    def getConfig(self):
        return g_eventsCache.getFalloutConfig(self.getBattleType())

    def isModeSelected(self):
        return self.isEnabled()

    def isBattleTypeSelected(self):
        return self.isEnabled() and self.getBattleType() in QUEUE_TYPE.FALLOUT

    def hasVehicleLvl8(self):
        return bool(self.__settings.get('hasVehicleLvl8', None))

    def setHasVehicleLvl8(self):
        self.__settings['hasVehicleLvl8'] = True
        g_settingsCore.serverSettings.setSection(SETTINGS_SECTIONS.FALLOUT, self.__settings)

    def hasVehicleLvl10(self):
        return bool(self.__settings.get('hasVehicleLvl10', None))

    def setHasVehicleLvl10(self):
        self.__settings['hasVehicleLvl10'] = True
        g_settingsCore.serverSettings.setSection(SETTINGS_SECTIONS.FALLOUT, self.__settings)

    def setHasVehicleLvls(self, hasVehicleLvl8 = False, hasVehicleLvl10 = False):
        self.__settings['hasVehicleLvl8'] = hasVehicleLvl8
        self.__settings['hasVehicleLvl10'] = hasVehicleLvl10
        g_settingsCore.serverSettings.setSection(SETTINGS_SECTIONS.FALLOUT, self.__settings)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\storage\fallout_storage.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:21:02 St�edn� Evropa (letn� �as)
