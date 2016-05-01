# 2016.05.01 15:22:33 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/IntroPage.py
import SoundGroups
from debug_utils import LOG_DEBUG, LOG_ERROR
from gui.Scaleform.daapi.view.meta.IntroPageMeta import IntroPageMeta
from gui.doc_loaders.GuiDirReader import GuiDirReader
from gui.shared import events

class IntroPage(IntroPageMeta):

    def __init__(self, _ = None):
        super(IntroPage, self).__init__()
        self.__movieFiles = GuiDirReader.getAvailableIntroVideoFiles()
        self.__soundValue = SoundGroups.g_instance.getMasterVolume() / 2

    def stopVideo(self):
        if self.__movieFiles is not None and len(self.__movieFiles):
            self.__showNextMovie()
            return
        else:
            LOG_DEBUG('Startup Video: STOP')
            self.__sendResult(True)
            return

    def handleError(self, data):
        self.__sendResult(False, 'Startup Video: ERROR - NetStream code = {0:>s}'.format(data))

    def _populate(self):
        super(IntroPage, self)._populate()
        if self.__movieFiles is not None and len(self.__movieFiles):
            self.__showNextMovie()
        else:
            self.__sendResult(False, 'There is no movie files for broadcast!')
        return

    def _dispose(self):
        super(IntroPage, self)._dispose()

    def __showNextMovie(self):
        self.__showMovie(self.__movieFiles.pop(0))

    def __showMovie(self, movie):
        LOG_DEBUG('Startup Video: START - movie = %s, sound volume = %d per cent' % (movie, self.__soundValue * 100))
        self.as_playVideoS({'source': movie,
         'volume': self.__soundValue})

    def __sendResult(self, isSuccess, msg = ''):
        """
        Call callback and send result of work
        @param isSuccess: is result of current component working has no errors
        @param msg: described reason of error
        """
        if not isSuccess:
            LOG_ERROR(msg)
        self.fireEvent(events.GlobalSpaceEvent(events.GlobalSpaceEvent.GO_NEXT))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\login\intropage.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:33 St�edn� Evropa (letn� �as)
