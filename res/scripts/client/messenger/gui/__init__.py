# 2016.05.01 15:24:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/__init__.py
from messenger.m_constants import MESSENGER_SCOPE

def setGUIEntries(decorator):
    from messenger.gui.Scaleform.LobbyEntry import LobbyEntry
    from messenger.gui.Scaleform.BattleEntry import BattleEntry
    decorator.setEntry(MESSENGER_SCOPE.LOBBY, LobbyEntry())
    decorator.setEntry(MESSENGER_SCOPE.BATTLE, BattleEntry())
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:50 Støední Evropa (letní èas)
