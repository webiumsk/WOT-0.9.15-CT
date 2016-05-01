# 2016.05.01 15:20:34 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/doc_loaders/__init__.py
from items import _xml

def readDict(xmlCtx, section, subsectionName, converter = lambda value: value.asString):
    result = {}
    for name, value in _xml.getChildren(xmlCtx, section, subsectionName):
        result[name] = converter(value)

    return result
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\doc_loaders\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:20:34 Støední Evropa (letní èas)
