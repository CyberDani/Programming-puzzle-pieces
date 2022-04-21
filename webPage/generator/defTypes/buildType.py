from enum import Enum

class BuildType(Enum):
    DO_NOT_BUILD = 0
    BUILD = 1
    REBUILD = 2