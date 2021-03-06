# 2016.05.01 15:20:11 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_control/minimap_utils.py
import string
import BigWorld
import Math
from constants import AOI
AOI_TO_FAR_TIME = 5.0
MINIMAP_SIZE = (210.0, 210.0)
MINIMAP_DIMENSION = 10.0
MINIMAP_COLUMN_OFFSET = 4
if AOI.ENABLE_MANUAL_RULES:
    AOI_ESTIMATE = AOI.VEHICLE_CIRCULAR_AOI_RADIUS - 50.0

    def isVehicleInAOI(matrix):
        ownPos = Math.Matrix(BigWorld.camera().invViewMatrix).translation
        entryPos = Math.Matrix(matrix).translation
        return (ownPos.x - entryPos.x) ** 2 + (ownPos.z - entryPos.z) ** 2 < AOI_ESTIMATE ** 2


else:
    AOI_ESTIMATE = 450.0

    def isVehicleInAOI(matrix):
        ownPos = Math.Matrix(BigWorld.camera().invViewMatrix).translation
        entryPos = Math.Matrix(matrix).translation
        return bool(abs(ownPos.x - entryPos.x) < AOI_ESTIMATE and abs(ownPos.z - entryPos.z) < AOI_ESTIMATE)


def makeCellIndex(localX, localY):
    column = int(MINIMAP_DIMENSION * localX / MINIMAP_SIZE[0])
    row = int(MINIMAP_DIMENSION * localY / MINIMAP_SIZE[1])
    return column * MINIMAP_DIMENSION + row


def getPositionByCellIndex(cellIndex, bottomLeft, upperRight):
    column, row = divmod(cellIndex, MINIMAP_DIMENSION)
    spaceSize = upperRight - bottomLeft
    return (column * spaceSize[0] / MINIMAP_DIMENSION - spaceSize[0] * 0.5, 0, -row * spaceSize[1] / MINIMAP_DIMENSION + spaceSize[1] * 0.5)


def getPositionByLocal(localX, localY, bottomLeft, upperRight):
    spaceSize = upperRight - bottomLeft
    x = (localX - MINIMAP_SIZE[0] * 0.5) / MINIMAP_SIZE[0] * spaceSize[0]
    z = -((localY - MINIMAP_SIZE[1] * 0.5) / MINIMAP_SIZE[1]) * spaceSize[1]
    return (x, 0.0, z)


def getCellName(cellIndex):
    column, row = divmod(cellIndex, int(MINIMAP_DIMENSION))
    if row < 8:
        name = string.ascii_uppercase[row]
    else:
        name = string.ascii_uppercase[row + 1]
    return '{}{}'.format(name, int((column + 1) % MINIMAP_DIMENSION))


def makePositionMatrix(position):
    matrix = Math.Matrix()
    matrix.setTranslate(position)
    return matrix


def makePointInBBoxMatrix(position, bottomLeft, upperRight):
    vector2 = (upperRight + bottomLeft) * 0.5
    matrix = Math.Matrix()
    matrix.setTranslate((vector2.x, 0.0, vector2.y))
    vector3 = matrix.applyPoint(position)
    matrix.setTranslate(vector3)
    return matrix


def makePointMatrixByCellIndex(cellIndex, bottomLeft, upperRight):
    return makePointInBBoxMatrix(getPositionByCellIndex(cellIndex, bottomLeft, upperRight), bottomLeft, upperRight)


def makePointMatrixByLocal(localX, localY, bottomLeft, upperRight):
    return makePointInBBoxMatrix(getPositionByLocal(localX, localY, bottomLeft, upperRight), bottomLeft, upperRight)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\battle_control\minimap_utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:20:12 St�edn� Evropa (letn� �as)
