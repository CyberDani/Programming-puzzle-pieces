import enum
from enum import Enum, unique

@unique
class BuildType(Enum):
    DO_NOT_BUILD = enum.auto()
    BUILD = enum.auto()
    REBUILD = enum.auto()
