class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    # maintain count of chars in s1
    # walk s2 with 2 pointers, return True once match is found
    # j - i = len(s1)
    
    # sanity check
    if len(s1) > len(s2):
      return False

    # count letters for s1 and s2[0:len(s1)]
    cnt1 = [0] * 26
    cnt2 = [0] * 26
    for i in range(len(s1)):
      cnt1[ord(s1[i])-97] += 1
      cnt2[ord(s2[i])-97] += 1
    
    i, j = 0, len(s1)
    while j < len(s2):
      # check whether letter counts match
      match = True
      for a, b in zip(cnt1, cnt2):
        if a != b:
          match = False
          break
      if match:
        return True
      # advance window by 1
      cnt2[ord(s2[i])-97] -= 1
      cnt2[ord(s2[j])-97] += 1
      i += 1
      j += 1

    # check letter count match for s2[-len(s1):]
    match = True
    for a, b in zip(cnt1, cnt2):
      if a != b:
        match = False
        break
    if match:
      return True

    return False

