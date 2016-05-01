# 2016.05.01 15:24:16 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/tooltips/skill.py
from gui.shared.tooltips import TOOLTIP_TYPE, ToolTipData, ToolTipAttrField
from debug_utils import LOG_DEBUG

class SkillTooltipData(ToolTipData):

    def __init__(self, context):
        super(SkillTooltipData, self).__init__(context, TOOLTIP_TYPE.SKILL)
        LOG_DEBUG('SkillTooltipData')
        self.fields = (ToolTipAttrField(self, 'name', 'userName'),
         ToolTipAttrField(self, 'shortDescr', 'shortDescription'),
         ToolTipAttrField(self, 'descr', 'description'),
         ToolTipAttrField(self, 'level'),
         ToolTipAttrField(self, 'type'),
         ToolTipAttrField(self, 'count'))


class BuySkillTooltipData(SkillTooltipData):

    def __init__(self, context):
        super(BuySkillTooltipData, self).__init__(context)
        self.fields = self.fields + (ToolTipAttrField(self, 'header'),)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\tooltips\skill.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:24:16 Støední Evropa (letní èas)
