from modules.paths import path


def getCurrentBranch():
  f = open(path.getProjectRootAbsolutePath() + "/.git/HEAD", "r")
  content = f.read().splitlines()
  for line in content:
    if line[0:4] == "ref:":
      return line.partition("refs/heads/")[2]
  raise Exception("No branch name had been found!")
