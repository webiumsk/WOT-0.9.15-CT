# 2016.05.01 15:21:10 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/settings/config.py
from constants import HAS_DEV_RESOURCES
_COMMON_RELEASE_PACKAGES = ('gui.Scaleform.daapi.view.common',)
_COMMON_DEBUG_PACKAGES = ('gui.development.ui.GUIEditor',)
_LOBBY_RELEASE_PACKAGES = ('gui.Scaleform.daapi.view.lobby', 'gui.Scaleform.daapi.view.lobby.barracks', 'gui.Scaleform.daapi.view.lobby.boosters', 'gui.Scaleform.daapi.view.lobby.clans', 'gui.Scaleform.daapi.view.lobby.crewOperations', 'gui.Scaleform.daapi.view.lobby.customization', 'gui.Scaleform.daapi.view.lobby.cyberSport', 'gui.Scaleform.daapi.view.lobby.exchange', 'gui.Scaleform.daapi.view.lobby.fortifications', 'gui.Scaleform.daapi.view.lobby.hangar', 'gui.Scaleform.daapi.view.lobby.header', 'gui.Scaleform.daapi.view.lobby.inputChecker', 'gui.Scaleform.daapi.view.lobby.messengerBar', 'gui.Scaleform.daapi.view.lobby.prb_windows', 'gui.Scaleform.daapi.view.lobby.profile', 'gui.Scaleform.daapi.view.lobby.server_events', 'gui.Scaleform.daapi.view.lobby.store', 'gui.Scaleform.daapi.view.lobby.techtree', 'gui.Scaleform.daapi.view.lobby.trainings', 'gui.Scaleform.daapi.view.lobby.vehiclePreview', 'gui.Scaleform.daapi.view.lobby.wgnc', 'gui.Scaleform.daapi.view.login', 'messenger.gui.Scaleform.view')
_LOBBY_DEBUG_PACKAGES = ('gui.development.ui.messenger.view.lobby',)
_BATTLE_RELEASE_PACKAGES = ()
_BATTLE_DEBUG_PACKAGES = ('gui.development.ui.Scaleform.daapi.view.battle', 'gui.development.ui.messenger.view.battle')
LOBBY_PACKAGES = _LOBBY_RELEASE_PACKAGES
BATTLE_PACKAGES = _BATTLE_RELEASE_PACKAGES
COMMON_PACKAGES = _COMMON_RELEASE_PACKAGES
if HAS_DEV_RESOURCES:
    LOBBY_PACKAGES += _LOBBY_DEBUG_PACKAGES
    BATTLE_PACKAGES += _BATTLE_DEBUG_PACKAGES
    COMMON_PACKAGES += _COMMON_DEBUG_PACKAGES
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\settings\config.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:21:10 St�edn� Evropa (letn� �as)
