# 2016.05.01 15:22:53 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TrainingFormMeta.py
from gui.Scaleform.framework.entities.View import View

class TrainingFormMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def joinTrainingRequest(self, id):
        """
        :param id:
        :return :
        """
        self._printOverrideError('joinTrainingRequest')

    def createTrainingRequest(self):
        """
        :return :
        """
        self._printOverrideError('createTrainingRequest')

    def onEscape(self):
        """
        :return :
        """
        self._printOverrideError('onEscape')

    def onLeave(self):
        """
        :return :
        """
        self._printOverrideError('onLeave')

    def as_setListS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setList(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\trainingformmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:53 Støední Evropa (letní èas)
