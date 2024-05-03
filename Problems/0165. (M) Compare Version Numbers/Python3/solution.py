class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    
    # split versions into revisions, convert strings to integers
    v1_int = list(map(int, version1.split('.')))
    v2_int = list(map(int, version2.split('.')))
    # compare revision pairs
    for v1_r, v2_r in zip(v1_int, v2_int):
      if v1_r > v2_r:
        return 1
      if v2_r > v1_r:
        return -1

    # no revisions left to compare
    if len(v1_int) == len(v2_int):
      return 0

    # check remaining revisions for non-zero value
    ret = 1 if len(v1_int) > len(v2_int) else -1
    rem = v1_int if ret == 1 else v2_int
    for rev in rem[min(len(v1_int), len(v2_int)):]:
      if rev:
        return ret

    # all remaining revisions were zero
    return 0

