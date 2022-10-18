import enum
from enum import Enum, unique

@unique
class FilePathCheckerActionType(Enum):
  ENSURE_FILE_EXISTS = enum.auto()
  DONT_CHECK_FILE_EXISTENCE = enum.auto()
