from modules.paths import path


def getRepoRootDirectory():
  return path.getGitRepoAbsolutePathEndingWithSlash()

def getCurrentBranch():
  f = open(getRepoRootDirectory() + "/.git/HEAD", "r")
  content = f.read().splitlines()
  for line in content:
    if line[0:4] == "ref:":
      return line.partition("refs/heads/")[2]
  raise Exception("No branch name had been found!")
