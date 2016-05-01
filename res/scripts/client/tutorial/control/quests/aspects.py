# 2016.05.01 15:25:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/control/quests/aspects.py
import weakref
from helpers import aop

class XpExchangeAspect(aop.Aspect):

    def __init__(self, trigger, *args, **kwargs):
        super(XpExchangeAspect, self).__init__()
        self.__triggerRef = weakref.ref(trigger)

    def atCall(self, cd):
        trigger = self.__triggerRef()
        if trigger is None:
            return
        else:
            trigger.toggle(isOn=trigger.isOn())
            return

    def clear(self):
        self.__triggerRef = None
        return


class StartXpExchangeAspect(aop.Aspect):

    def __init__(self, trigger, *args, **kwargs):
        super(StartXpExchangeAspect, self).__init__()
        self.__triggerRef = weakref.ref(trigger)

    def atCall(self, cd):
        trigger = self.__triggerRef()
        if trigger is not None:
            trigger.registerRequest()
        return

    def clear(self):
        self.__triggerRef = None
        return


class XpExchangePointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.shared.gui_items.processors.common', 'FreeXPExchanger', '_successHandler')


class StartXpExchangePointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.shared.gui_items.processors.common', 'FreeXPExchanger', '_request')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\control\quests\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:25:33 Støední Evropa (letní èas)
