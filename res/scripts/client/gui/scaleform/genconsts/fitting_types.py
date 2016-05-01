# 2016.05.01 15:23:02 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/genConsts/FITTING_TYPES.py


class FITTING_TYPES(object):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    null
    """
    OPTIONAL_DEVICE = 'optionalDevice'
    EQUIPMENT = 'equipment'
    SHELL = 'shell'
    VEHICLE = 'vehicle'
    MODULE = 'module'
    ORDER = 'order'
    STORE_SLOTS = [VEHICLE,
     MODULE,
     SHELL,
     OPTIONAL_DEVICE,
     EQUIPMENT]
    ARTEFACT_SLOTS = [OPTIONAL_DEVICE, EQUIPMENT]
    VEHICLE_GUN = 'vehicleGun'
    VEHICLE_TURRET = 'vehicleTurret'
    VEHICLE_CHASSIS = 'vehicleChassis'
    VEHICLE_ENGINE = 'vehicleEngine'
    VEHICLE_RADIO = 'vehicleRadio'
    MANDATORY_SLOTS = [VEHICLE_GUN,
     VEHICLE_TURRET,
     VEHICLE_CHASSIS,
     VEHICLE_ENGINE,
     VEHICLE_RADIO]
    TARGET_CURRENT = 1
    TARGET_IN_INVENTORY = 2
    TARGET_OTHER = 3
    ITEM_TARGETS = [TARGET_CURRENT, TARGET_IN_INVENTORY, TARGET_OTHER]
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\genconsts\fitting_types.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:23:02 St�edn� Evropa (letn� �as)
