# 2016.05.01 15:20:42 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/miniclient/lobby/hangar/__init__.py
import pointcuts as _pointcuts

def configure_pointcuts(config):
    _pointcuts.DisableTankServiceButtons(config)
    _pointcuts.MaintenanceButtonFlickering(config)
    _pointcuts.DeviceButtonsFlickering(config)
    _pointcuts.ShowMiniclientInfo()
    _pointcuts.TankHangarStatus(config)
    _pointcuts.TankModelHangarVisibility(config)
    _pointcuts.EnableCrew(config)
    _pointcuts.ChangeLobbyMenuTooltip()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\lobby\hangar\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:20:42 St�edn� Evropa (letn� �as)
