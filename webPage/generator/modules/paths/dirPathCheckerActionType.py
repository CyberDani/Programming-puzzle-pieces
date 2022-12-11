import enum
from enum import Enum, unique

@unique
class DirPathCheckerActionType(Enum):
  ENSURE_DIR_AND_FILES_EXIST = enum.auto()
  ENSURE_DIR_EXISTS_ONLY = enum.auto()
  DO_NOT_CHECK_DIR_EXISTENCE = enum.auto()
  CREATE_DIR_IF_NOT_EXISTS = enum.auto()
