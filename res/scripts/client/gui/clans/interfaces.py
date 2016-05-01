# 2016.05.01 15:20:23 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/clans/interfaces.py


class IClanListener(object):

    def onClanStateChanged(self, oldStateID, newStateID):
        pass

    def onClanInvitesCountReceived(self, clanDbID, invitesCount):
        pass

    def onClanAppsCountReceived(self, clanDbID, appsCount):
        pass

    def onClanInfoReceived(self, clanDbID, clanInfo):
        pass

    def onClanWebVitalInfoChanged(self, clanDbID, fieldName, value):
        pass

    def onAccountClanProfileChanged(self, profile):
        pass

    def onAccountClanInfoReceived(self, info):
        pass

    def onAccountInvitesReceived(self, invites):
        pass

    def onAccountAppsReceived(self, applications):
        pass

    def onAccountWebVitalInfoChanged(self, fieldName, value):
        pass

    def onClanAppStateChanged(self, appId, state):
        pass

    def onClanInvitesStateChanged(self, inviteIds, state):
        pass

    def onWgncNotificationReceived(self, notifID, item):
        pass

    def onMembersListChanged(self, members):
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\clans\interfaces.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:20:23 Støední Evropa (letní èas)
