#A decomposition of moves into component pickups or placements

from enum import Enum


class MovementType(Enum):
    home = 1
    up = 2
    down = 3

class Movement:
    def __init__(self, movement_type, square):
        self.movement_type = movement_type  # MovementType
        self.square = square    # string eg E8
