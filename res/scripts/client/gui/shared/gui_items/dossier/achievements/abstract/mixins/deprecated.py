# 2016.05.01 15:24:02 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/mixins/Deprecated.py
from gui.shared.gui_items.dossier.achievements import validators

class Deprecated(object):

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\abstract\mixins\deprecated.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:02 Støední Evropa (letní èas)
