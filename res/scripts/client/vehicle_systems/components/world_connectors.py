# 2016.05.01 15:25:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/vehicle_systems/components/world_connectors.py
import BigWorld
from vehicle_systems import assembly_utility
from vehicle_systems.tankStructure import TankPartNames

class GunRotatorConnector(assembly_utility.Component):

    def __init__(self, model):
        soundEffect = BigWorld.player().gunRotator.soundEffect
        if soundEffect is not None:
            soundEffect.connectSoundToMatrix(model.node(TankPartNames.TURRET))
        return

    def destroy(self):
        self.processVehicleDeath(None)
        return

    def processVehicleDeath(self, vehicleDamageState):
        soundEffect = BigWorld.player().gunRotator.soundEffect
        if soundEffect is not None:
            soundEffect.lockSoundMatrix()
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\vehicle_systems\components\world_connectors.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:25:46 Støední Evropa (letní èas)
