# 2016.05.01 15:20:18 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_control/consumables/__init__.py
from gui.battle_control.consumables import opt_devices_ctrl
from gui.battle_control.consumables import ammo_ctrl
from gui.battle_control.consumables import equipment_ctrl

def createAmmoCtrl(isReplayPlaying, isReplayRecording):
    import BattleReplay
    if isReplayRecording:
        return ammo_ctrl.AmmoReplayRecorder(BattleReplay.g_replayCtrl)
    if isReplayPlaying:
        return ammo_ctrl.AmmoReplayPlayer(BattleReplay.g_replayCtrl)
    return ammo_ctrl.AmmoController()


def createEquipmentCtrl(isReplayPlaying):
    if isReplayPlaying:
        clazz = equipment_ctrl.EquipmentsReplayPlayer
    else:
        clazz = equipment_ctrl.EquipmentsController
    return clazz()


def createOptDevicesCtrl():
    return opt_devices_ctrl.OptionalDevicesController()


__all__ = ('createAmmoCtrl', 'createEquipmentCtrl', 'createOptDevicesCtrl')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\battle_control\consumables\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:20:18 St�edn� Evropa (letn� �as)
