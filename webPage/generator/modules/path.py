from defTypes import dirPathType

def getGitRepoAbsolutePathEndingWithSlash():
  return dirPathType.DirectoryRelPathType.GIT_REPOSITORY.value.getAbsolutePathEndingWithSlash()
