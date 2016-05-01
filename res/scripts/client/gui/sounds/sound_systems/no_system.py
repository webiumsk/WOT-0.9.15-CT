# 2016.05.01 15:24:27 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/sounds/sound_systems/no_system.py
from gui.sounds.abstract import SoundSystemAbstract
from gui.sounds.sound_constants import SoundSystems

class NoSoundSystem(SoundSystemAbstract):

    def getID(self):
        return SoundSystems.UNKNOWN
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\sounds\sound_systems\no_system.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:27 Støední Evropa (letní èas)
