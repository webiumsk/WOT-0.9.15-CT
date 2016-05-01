# 2016.05.01 15:22:48 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileSummaryWindowMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSummary import ProfileSummary

class ProfileSummaryWindowMeta(ProfileSummary):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ProfileSummary
    null
    """

    def openClanStatistic(self):
        """
        :return :
        """
        self._printOverrideError('openClanStatistic')

    def openClubProfile(self, clubDbID):
        """
        :param clubDbID:
        :return :
        """
        self._printOverrideError('openClubProfile')

    def as_setClanDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanData(data)

    def as_setClubDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClubData(data)

    def as_setClanEmblemS(self, source):
        """
        :param source:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(source)

    def as_setClubEmblemS(self, source):
        """
        :param source:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClubEmblem(source)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\profilesummarywindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:48 Støední Evropa (letní èas)
