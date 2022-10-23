from modules import checks

from enum import Enum, unique, auto
import requests
import string

from dataclasses import dataclass

@unique
class GitBlobType(Enum):
  BLOB = auto()
  TREE = auto()

@dataclass
class GithubBlob:
  relPath: str
  mode: int
  type: GitBlobType
  sha: str
  size: int
  url: str

@unique
class RepoBranchType(Enum):
  MASTER = "master"
  DEVEL = "devel"


githubUser = "CyberDani"
githubRepo = "Programming-puzzle-pieces"
githubApiBaseUrl = "https://api.github.com"

# calculate these values only once to reduce the number of requests. Their value most probably
# will not change anyway within 1 run
treeShas = {}
filesAndDirs = {}

def getTreeSha(repoBranchType):
  """Return values:\n
* found: True | False \n
* headTreeSha: empty string if not found"""
  checks.checkIfType(repoBranchType, RepoBranchType)
  if repoBranchType in treeShas:
    return True, treeShas[repoBranchType]
  notFoundResult = (False, "")
  url = githubApiBaseUrl + "/repos/" + githubUser + "/" + githubRepo + "/branches/" + repoBranchType.value
  try:
    response = requests.get(url)
    if response.status_code != 200:
      return notFoundResult
    response = response.json()
    # if any key not exists, it will throw an exception and as a result return notFound
    result = response['commit']['commit']['tree']['sha']
  except:
    return notFoundResult
  allCharsAreHexDigits = all(c in string.hexdigits for c in result)
  if not allCharsAreHexDigits:
    return  notFoundResult
  treeShas[repoBranchType] = result
  return True, result

# Example:
#{
#  "path": ".github/FUNDING.yml",
#  "mode": "100644",
#  "type": "blob",
#  "sha": "d65237c7582dbc0b49d843b9994e15a0a66d0c11",
#  "size": 671,  <--- size is present for only blob type
#  "url": "https://api.github.com/repos/CyberDani/Programming-puzzle-pieces/git/blobs/d65237c7582dbc0b49d843b9994e15a0a66d0c11"
#}
def getGithubBlobFromJsonObject(json):
  """Return values: \n
* corrupt: True | False (only the presence of the fields is validated, nothing else)
* githubBlob: None if corrupt"""
  checks.checkIfType(json, dict)
  corruptResult = (True, None)
  try:
    if "path" not in json or "mode" not in json or "type" not in json or "sha" not in json or "url" not in json:
      return corruptResult
    path = json['path']
    mode = json['mode']
    blob = json['type']
    blobType = GitBlobType.BLOB
    if blob == "tree":
      blobType = GitBlobType.TREE
    sha = json['sha']
    size = -1  # default value, means that there is no size
    if blobType == GitBlobType.BLOB:
      if "size" not in json:
        return corruptResult
      size = json['size']
    url = json['url']
    result = GithubBlob(relPath = path, mode = mode, type=blobType, sha=sha, size=size, url=url)
    return False, result
  except:
    return corruptResult

def getAllBlobs(repoBranchType):
  """Return values:\n
* found: True | False \n
* listOfDirsAndFiles: empty list if not found"""
  notFoundResult = (False, [])
  if repoBranchType in filesAndDirs:
    return True, filesAndDirs[repoBranchType]
  found, treeSha = getTreeSha(repoBranchType)
  if not found:
    return notFoundResult
  result = []
  url = githubApiBaseUrl + "/repos/" + githubUser + "/" + githubRepo + "/git/trees/" + treeSha + "?recursive=1"
  try:
    response = requests.get(url)
    if response.status_code != 200:
      return notFoundResult
    response = response.json()
    # if any key not exists, it will throw an exception and as a result return notFound
    jsonTree = response['tree']
    for pathItem in jsonTree:
      corrupt, blob = getGithubBlobFromJsonObject(pathItem)
      if corrupt:
        return notFoundResult
      result.append(blob)
  except:
    return notFoundResult
  filesAndDirs[repoBranchType] = result
  return True, result

def getBlobsByFileName(repoBranchType, fileName):
  """Return values:\n
* found: True | False \n
* listOfBlobs: empty list if not found"""
  checks.checkIfString(fileName, 1, 120)
  found, listOfBlobs = getAllBlobs(repoBranchType)
  notFoundResult = (False, [])
  if not found:
    return notFoundResult
  result = []
  for blob in listOfBlobs:
    if blob.type == GitBlobType.TREE:
      continue
    blobFileName = blob.relPath.split("/")[-1]
    if blobFileName == fileName:
      result.append(blob)
  if not result:
    return notFoundResult
  return True, result
