# 2016.05.01 15:22:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SimpleWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SimpleWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onBtnClick(self, action):
        """
        :param action:
        :return :
        """
        self._printOverrideError('onBtnClick')

    def as_setWindowTitleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_setTextS(self, header, descrition):
        """
        :param header:
        :param descrition:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setText(header, descrition)

    def as_setImageS(self, imgPath, imgBottomMargin):
        """
        :param imgPath:
        :param imgBottomMargin:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setImage(imgPath, imgBottomMargin)

    def as_setButtonsS(self, buttonsList, align, btnWidth):
        """
        :param buttonsList:
        :param align:
        :param btnWidth:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setButtons(buttonsList, align, btnWidth)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\simplewindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:51 Støední Evropa (letní èas)
