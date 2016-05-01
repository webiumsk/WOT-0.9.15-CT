# 2016.05.01 15:22:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CalendarMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CalendarMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onMonthChanged(self, rawDate):
        """
        :param rawDate:
        :return :
        """
        self._printOverrideError('onMonthChanged')

    def onDateSelected(self, rawDate):
        """
        :param rawDate:
        :return :
        """
        self._printOverrideError('onDateSelected')

    def formatYMHeader(self, rawDate):
        """
        :param rawDate:
        :return String:
        """
        self._printOverrideError('formatYMHeader')

    def as_openMonthS(self, rawDate):
        """
        :param rawDate:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_openMonth(rawDate)

    def as_selectDateS(self, rawDate):
        """
        :param rawDate:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_selectDate(rawDate)

    def as_updateMonthEventsS(self, items):
        """
        :param items:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateMonthEvents(items)

    def as_setCalendarMessageS(self, message):
        """
        :param message:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCalendarMessage(message)

    def as_setMinAvailableDateS(self, rawDate):
        """
        :param rawDate:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMinAvailableDate(rawDate)

    def as_setMaxAvailableDateS(self, rawDate):
        """
        :param rawDate:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxAvailableDate(rawDate)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\calendarmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:22:37 Støední Evropa (letní èas)
