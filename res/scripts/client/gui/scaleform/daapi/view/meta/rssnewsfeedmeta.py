# 2016.05.01 15:22:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RssNewsFeedMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RssNewsFeedMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def openBrowser(self, linkToOpen):
        """
        :param linkToOpen:
        :return :
        """
        self._printOverrideError('openBrowser')

    def as_updateFeedS(self, feed):
        """
        :param feed:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateFeed(feed)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\rssnewsfeedmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:50 Støední Evropa (letní èas)
