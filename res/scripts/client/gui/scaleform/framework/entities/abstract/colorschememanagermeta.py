# 2016.05.01 15:22:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ColorSchemeManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ColorSchemeManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def getColorScheme(self, schemeName):
        """
        :param schemeName:
        :return Object:
        """
        self._printOverrideError('getColorScheme')

    def as_updateS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\colorschememanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:57 Støední Evropa (letní èas)
