# 2016.05.01 15:22:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/logitech/logo_screen.py
from gui.Scaleform.daapi.view.logitech.LogitechMonitorMeta import LogitechMonitorMonoScreenMeta, LogitechMonitorColoredScreenMeta
from helpers import i18n

class LogitechMonitorLogoMonoScreen(LogitechMonitorMonoScreenMeta):

    def _onLoaded(self):
        self.as_setText(i18n.makeString('#menu:login/version'))


class LogitechMonitorLogoColoredScreen(LogitechMonitorColoredScreenMeta):
    pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\logitech\logo_screen.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:35 Støední Evropa (letní èas)
