# 2016.05.01 15:24:20 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/utils/SelectorBattleTypesUtils.py
from account_helpers.AccountSettings import AccountSettings, KNOWN_SELECTOR_BATTLES

def setBattleTypeAsKnown(bType):
    selectorKnownBattles = set(AccountSettings.getSettings(KNOWN_SELECTOR_BATTLES))
    selectorKnownBattles.add(bType)
    AccountSettings.setSettings(KNOWN_SELECTOR_BATTLES, selectorKnownBattles)


def isKnownBattleType(bType):
    selectorKnownBattles = set(AccountSettings.getSettings(KNOWN_SELECTOR_BATTLES))
    return bType in selectorKnownBattles
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\utils\selectorbattletypesutils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:21 Støední Evropa (letní èas)
