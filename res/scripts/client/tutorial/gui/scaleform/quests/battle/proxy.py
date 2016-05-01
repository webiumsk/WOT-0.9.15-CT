# 2016.05.01 15:25:42 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/quests/battle/proxy.py
from tutorial.gui import GUIProxy

class BattleQuestsProxy(GUIProxy):

    def __init__(self):
        super(BattleQuestsProxy, self).__init__()

    def init(self):
        self.onGUILoaded()
        return True

    def clear(self):
        self.clearChapterInfo()

    def getSceneID(self):
        return 'Battle'

    def playEffect(self, effectName, args, itemRef = None, containerRef = None):
        return False

    def isEffectRunning(self, effectName, effectID = None):
        return False
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\gui\scaleform\quests\battle\proxy.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:25:42 Støední Evropa (letní èas)
