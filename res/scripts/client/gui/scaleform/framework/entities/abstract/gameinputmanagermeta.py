# 2016.05.01 15:22:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/GameInputManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class GameInputManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def handleGlobalKeyEvent(self, keyCode, eventType):
        """
        :param keyCode:
        :param eventType:
        :return :
        """
        self._printOverrideError('handleGlobalKeyEvent')

    def as_addKeyHandlerS(self, keyCode, eventType, ignoreText, cancelEventType):
        """
        :param keyCode:
        :param eventType:
        :param ignoreText:
        :param cancelEventType:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_addKeyHandler(keyCode, eventType, ignoreText, cancelEventType)

    def as_clearKeyHandlerS(self, keyCode, eventType):
        """
        :param keyCode:
        :param eventType:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_clearKeyHandler(keyCode, eventType)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\gameinputmanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:58 Støední Evropa (letní èas)
