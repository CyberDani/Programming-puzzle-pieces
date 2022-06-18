import enum
from enum import Enum, unique

@unique
class DirPathCheckerActionType(Enum):
  ENSURE_PATH_AND_FILES_EXIST = enum.auto()
  ENSURE_PATH_EXISTS_ONLY = enum.auto()
