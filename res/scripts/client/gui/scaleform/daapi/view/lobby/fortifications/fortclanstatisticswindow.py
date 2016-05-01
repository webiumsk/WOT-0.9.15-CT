# 2016.05.01 15:21:52 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/FortClanStatisticsWindow.py
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.meta.FortClanStatisticsWindowMeta import FortClanStatisticsWindowMeta

class FortClanStatisticsWindow(FortClanStatisticsWindowMeta):

    def __init__(self, ctx = None):
        super(FortClanStatisticsWindow, self).__init__()
        self.data = ctx
        self.data.onDataChanged += self.onDataChanged

    def _populate(self):
        super(FortClanStatisticsWindow, self)._populate()
        LOG_DEBUG('FortClanStatisticsWindow | _populate', self.data.getData())
        self.as_setDataS(self.data.getData())

    def _dispose(self):
        self.data.stopFortListening()
        super(FortClanStatisticsWindow, self)._dispose()

    def onDataChanged(self):
        self.as_setDataS(self.data.getData())

    def onWindowClose(self):
        self.destroy()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\fortifications\fortclanstatisticswindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:21:52 Støední Evropa (letní èas)
