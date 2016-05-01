# 2016.05.01 15:24:00 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/SentinelAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class SentinelAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(SentinelAchievement, self).__init__('sentinelMedal', _AB.TEAM_7X7, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'sentinel')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\sentinelachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:00 Støední Evropa (letní èas)
