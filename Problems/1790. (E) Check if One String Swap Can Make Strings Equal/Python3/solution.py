class Solution:
  def areAlmostEqual(self, s1: str, s2: str) -> bool:
    # frequency map

    d = 0
    for c1, c2 in zip(s1, s2):
      if c1 != c2:
        d += 1
        if d > 2:
          return False

    return Counter(s1) == Counter(s2)

