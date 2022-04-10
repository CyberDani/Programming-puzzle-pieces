from modules import checks

# <endsWithStr> must be after <startsWithStr>
# Return empty string if 
def getStringStartsWithEndsWithNoOverlap(src, startsWithStr, endsWithStr):
  checks.checkIfString(src, 2, 500)
  checks.checkIfString(startsWithStr, 1, 500)
  checks.checkIfString(endsWithStr, 1, 500)
  startIdx = src.find(startsWithStr)
  if startIdx == -1:
    return ""
  idxAdd = startIdx + len(startsWithStr)
  originalSrc = src
  src = src[idxAdd:]
  endIdx = src.find(endsWithStr)
  if endIdx == -1:
    return ""
  endIdx += idxAdd + len(endsWithStr)
  return originalSrc[startIdx:endIdx]