# 2016.05.01 15:22:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsPersonalWelcomeViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsPersonalWelcomeViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def success(self):
        """
        :return :
        """
        self._printOverrideError('success')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_showMiniClientInfoS(self, description, hyperlink):
        """
        :param description:
        :param hyperlink:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\questspersonalwelcomeviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:49 Støední Evropa (letní èas)
