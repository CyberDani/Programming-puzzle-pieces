import enum
from enum import Enum, unique

@unique
class AppDecisionType(Enum):
    STOP_APP = enum.auto()
    CONTINUE_RUNNING = enum.auto()
