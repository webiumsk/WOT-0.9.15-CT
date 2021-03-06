# 2016.05.01 15:20:42 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/miniclient/lobby/MiniclientDescriptionWindow.py
import os
from gui import GUI_SETTINGS
from gui.game_control import getBrowserCtrl
from gui.shared import g_eventBus, events
from helpers.i18n import makeString as _ms

class MiniclientDescriptionWindow(object):

    def __init__(self):
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__openDescriptionInBrowser)

    def __openDescriptionInBrowser(self, event):
        current_working_dir = os.getcwd()
        getBrowserCtrl().load(url='{0}/$LANGUAGE_CODE/greeting/mini_wot/'.format(GUI_SETTINGS.miniclient['webBridgeRootURL']), title=_ms('#miniclient:hangar/miniclient_description_window/title'), browserSize=(780, 450), showCloseBtn=True, showActionBtn=False, isAsync=True)(lambda success: True)
        g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__openDescriptionInBrowser)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\lobby\miniclientdescriptionwindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:20:42 St�edn� Evropa (letn� �as)
