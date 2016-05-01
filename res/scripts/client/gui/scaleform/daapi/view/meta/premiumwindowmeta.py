# 2016.05.01 15:22:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PremiumWindowMeta.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta

class PremiumWindowMeta(SimpleWindowMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleWindowMeta
    null
    """

    def onRateClick(self, rateId):
        """
        :param rateId:
        :return :
        """
        self._printOverrideError('onRateClick')

    def as_setHeaderS(self, prc, bonus1, bonus2):
        """
        :param prc:
        :param bonus1:
        :param bonus2:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(prc, bonus1, bonus2)

    def as_setRatesS(self, header, rates, selectedRateId):
        """
        :param header:
        :param rates:
        :param selectedRateId:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRates(header, rates, selectedRateId)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\premiumwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:47 Støední Evropa (letní èas)
