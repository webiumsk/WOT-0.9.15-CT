# 2016.05.01 15:31:42 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/plat-mac/terminalcommand.py
"""terminalcommand.py -- A minimal interface to Terminal.app.

To run a shell command in a new Terminal.app window:

    import terminalcommand
    terminalcommand.run("ls -l")

No result is returned; it is purely meant as a quick way to run a script
with a decent input/output window.
"""
from warnings import warnpy3k
warnpy3k('In 3.x, the terminalcommand module is removed.', stacklevel=2)
import time
import os
from Carbon import AE
from Carbon.AppleEvents import *
TERMINAL_SIG = 'trmx'
START_TERMINAL = '/usr/bin/open /Applications/Utilities/Terminal.app'
SEND_MODE = kAENoReply

def run(command):
    """Run a shell command in a new Terminal.app window."""
    termAddress = AE.AECreateDesc(typeApplicationBundleID, 'com.apple.Terminal')
    theEvent = AE.AECreateAppleEvent(kAECoreSuite, kAEDoScript, termAddress, kAutoGenerateReturnID, kAnyTransactionID)
    commandDesc = AE.AECreateDesc(typeChar, command)
    theEvent.AEPutParamDesc(kAECommandClass, commandDesc)
    try:
        theEvent.AESend(SEND_MODE, kAENormalPriority, kAEDefaultTimeout)
    except AE.Error as why:
        if why[0] != -600:
            raise
        os.system(START_TERMINAL)
        time.sleep(1)
        theEvent.AESend(SEND_MODE, kAENormalPriority, kAEDefaultTimeout)


if __name__ == '__main__':
    run('ls -l')
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\terminalcommand.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:31:43 St�edn� Evropa (letn� �as)
