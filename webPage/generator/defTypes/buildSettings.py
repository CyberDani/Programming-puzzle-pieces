import io
from dataclasses import dataclass

from defTypes import buildType
from defTypes import dbBranchType
from modules import counter

@dataclass
class BuildSettings:
    buildOption: buildType.BuildType
    dbBranch: dbBranchType.DbBranchType
    stepsCounter: counter.SimpleCounter
    htmlOutputFile: io.TextIOBase
    indentDepth: int = 1

    def __post_init__(self):
        if not isinstance(self.dbBranch, dbBranchType.DbBranchType):
            raise Exception("Type dbBranchType.DbBranchType mismatch!")
        if not isinstance(self.buildOption, buildType.BuildType):
            raise Exception("Type buildType.BuildType mismatch!")
        if not isinstance(self.htmlOutputFile, io.TextIOBase):
            raise Exception("Type io.TextIOBase mismatch!")
        if not isinstance(self.indentDepth, int):
            raise Exception("Type int mismatch!")
        if not isinstance(self.stepsCounter, counter.SimpleCounter):
            raise Exception("Type counter.SimpleCounter mismatch!")
