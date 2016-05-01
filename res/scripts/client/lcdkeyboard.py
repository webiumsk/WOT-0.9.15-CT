# 2016.05.01 15:19:26 Støední Evropa (letní èas)
# Embedded file name: scripts/client/LcdKeyboard.py
import BigWorld
g_instance = None

class LCD_KEY:
    LEFT = 256
    RIGHT = 512
    OK = 1024
    CANCEL = 2048
    UP = 4096
    DOWN = 8192
    MENU = 16384


def enableLcdKeyboardSpecificKeys(bValue):
    global g_instance
    if bValue:
        if g_instance is not None:
            return True
        g_instance = BigWorld.WGLcdKeyboard()
        if not g_instance.isValid():
            g_instance.destroy()
            g_instance = None
            return False
    else:
        if g_instance is None:
            return True
        g_instance.destroy()
        g_instance = None
    return True


def getKeys(mask = 4294967295L):
    if g_instance is None:
        return 0
    else:
        return g_instance.getKeys() & mask


def finalize():
    enableLcdKeyboardSpecificKeys(False)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\lcdkeyboard.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:19:26 Støední Evropa (letní èas)
