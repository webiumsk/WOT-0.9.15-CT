# 2016.05.01 15:22:34 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/logitech/battle_loading.py
from gui.Scaleform import getPathForFlash, SCALEFORM_SWF_PATH
from gui.Scaleform.daapi.view.logitech.LogitechMonitorMeta import LogitechMonitorBattleLoadingColoredScreenMeta, LogitechMonitorMonoScreenMeta
from gui.battle_control import g_sessionProvider

def _getData():
    """
    :return: (arenaDescription, arenaTypeName, icon)
    """
    ctx = g_sessionProvider.getCtx()
    if ctx is not None:
        return (ctx.getArenaDescriptionString(), ctx.getArenaTypeName(), ctx.getArenaScreenIcon())
    else:
        return (None, None, None)


class LogitechMonitorBattleLoadingMonoScreen(LogitechMonitorMonoScreenMeta):

    def _onLoaded(self):
        arenaDescription, arenaTypeName, _ = _getData()
        text = '{}\r\n{}'.format(arenaTypeName, arenaDescription)
        self.as_setText(text)


class LogitechMonitorBattleLoadingColoredScreen(LogitechMonitorBattleLoadingColoredScreenMeta):

    def _onLoaded(self):
        arenaDescription, arenaTypeName, icon = _getData()
        icon = getPathForFlash(icon, base=SCALEFORM_SWF_PATH)
        self.as_setMap(arenaTypeName, arenaDescription, icon)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\logitech\battle_loading.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:34 Støední Evropa (letní èas)
