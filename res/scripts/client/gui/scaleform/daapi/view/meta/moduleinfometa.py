# 2016.05.01 15:22:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ModuleInfoMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ModuleInfoMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onCancelClick(self):
        """
        :return :
        """
        self._printOverrideError('onCancelClick')

    def onActionButtonClick(self):
        """
        :return :
        """
        self._printOverrideError('onActionButtonClick')

    def as_setModuleInfoS(self, moduleInfo):
        """
        :param moduleInfo:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setModuleInfo(moduleInfo)

    def as_setActionButtonS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setActionButton(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\moduleinfometa.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:46 Støední Evropa (letní èas)
