# 2016.05.01 15:22:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/BaseDAAPIModuleMeta.py
from gui.Scaleform.framework.entities.DAAPIEntity import DAAPIEntity

class BaseDAAPIModuleMeta(DAAPIEntity):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends DAAPIEntity
    null
    """

    def as_populateS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_populate()

    def as_disposeS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\basedaapimodulemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:57 Støední Evropa (letní èas)
