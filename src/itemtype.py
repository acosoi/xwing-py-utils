from enum import Enum

# Item types that exist in X-Wing (does not include dice, tokens or rulers)
class ItemType(Enum):
    SHIP = 1
    PILOT = 2
    UPGRADE = 3
    REFERENCE_CARD = 4
    CONDITION = 5
    DAMAGE_CORE = 6
    DAMAGE_CORE2 = 7
    DAMAGE_REBEL_TRANSPORT = 8
