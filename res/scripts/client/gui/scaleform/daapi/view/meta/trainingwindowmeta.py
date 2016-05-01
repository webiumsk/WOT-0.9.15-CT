# 2016.05.01 15:22:53 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TrainingWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TrainingWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def updateTrainingRoom(self, key, time, isPrivate, description):
        """
        :param key:
        :param time:
        :param isPrivate:
        :param description:
        :return :
        """
        self._printOverrideError('updateTrainingRoom')

    def as_setDataS(self, info, mapsData):
        """
        :param info:
        :param mapsData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(info, mapsData)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\trainingwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:53 Støední Evropa (letní èas)
