from enum import Enum, auto

class State(Enum):
    IDLE = auto()
    MOVING = auto()
    MAINTENANCE = auto()
