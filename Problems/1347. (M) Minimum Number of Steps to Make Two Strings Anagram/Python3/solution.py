class Solution:
  def minSteps(self, s: str, t: str) -> int:
    # greedy algorithm using dictionaries

    tgt_f, f = Counter(s), Counter(t)
    ret = 0
    for k, v in tgt_f.items():
      ret += v - f[k] if v > f[k] else 0

    return ret

