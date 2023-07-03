class Solution:
  def buddyStrings(self, s: str, goal: str) -> bool:
    if len(s) != len(goal):
      return False
    src, tgt = Counter(), Counter()
    mismatch = 0
    for i, j in zip(s, goal):
      src[i] += 1
      tgt[j] += 1
      if i != j:
        mismatch += 1
    if src != tgt:
      return False
    if not mismatch and max(src.values()) >= 2:
      return True
    if mismatch == 2:
      return True
    return False
  
