import enum
from enum import Enum, unique

@unique
class DbBranchType(Enum):
  MASTER = enum.auto()
  DEVEL = enum.auto()
