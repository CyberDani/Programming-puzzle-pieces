from modules.paths.values import possibleFilePathTypes as fTypes

def checkIfFileType(value):
  for fileType in fTypes.filePathTypes:
    if type(value) == fileType:
      return
  raise Exception("Type missmatch using '{}'!".format(str(type(value))))
