# 2016.05.01 15:22:42 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortChoiceDivisionWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortChoiceDivisionWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def selectedDivision(self, divisionID):
        """
        :param divisionID:
        :return :
        """
        self._printOverrideError('selectedDivision')

    def changedDivision(self, divisionID):
        """
        :param divisionID:
        :return :
        """
        self._printOverrideError('changedDivision')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortchoicedivisionwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:42 Støední Evropa (letní èas)
