# 2016.05.01 15:26:08 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/invites.py
from enumerations import Enumeration
INVITE_TYPES = Enumeration('InviteTypes', ['BARTER',
 'TEAM',
 'CLAN',
 'TRAINING_ROOM',
 'PREBATTLE'])
_g_invitesConfig = {INVITE_TYPES.BARTER.index(): {'TTL': 900,
                               'keepInArchive': 3600,
                               'checkIgnore': True},
 INVITE_TYPES.TEAM.index(): {'TTL': -1,
                             'keepInArchive': -1,
                             'checkIgnore': True},
 INVITE_TYPES.CLAN.index(): {'TTL': -1,
                             'keepInArchive': -1,
                             'checkIgnore': True},
 INVITE_TYPES.TRAINING_ROOM.index(): {'TTL': 900,
                                      'keepInArchive': 3600,
                                      'checkIgnore': True},
 INVITE_TYPES.PREBATTLE.index(): {'TTL': 900,
                                  'keepInArchive': 3600,
                                  'checkIgnore': True}}
_g_defaultInviteConfig = {'TTL': -1,
 'keepInArchive': -1,
 'checkIgnore': True}

def getInviteConfig(inviteTypeIdx):
    return _g_invitesConfig.get(inviteTypeIdx, _g_defaultInviteConfig)


INVITE_STATUS = Enumeration('Invite statuses', ['accepted',
 'rejected',
 'invalid',
 'invalidTTL'])
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\invites.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:26:08 St�edn� Evropa (letn� �as)
