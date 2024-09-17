class Solution:
  def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    # dictionaries

    s1_w, s2_w = Counter(s1.split()), Counter(s2.split())
    res = []
    for k, v in s1_w.items():
      if k not in s2_w and v == 1:
        res.append(k)
    for k, v in s2_w.items():
      if k not in s1_w and v == 1:
        res.append(k)

    return res

