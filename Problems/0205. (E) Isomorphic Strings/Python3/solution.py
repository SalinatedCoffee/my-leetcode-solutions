class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    # record mapping using dictionary

    # stot[i] = j character i in s maps to character j in t
    stot = {}
    # set of characters in t that have been mapped
    t_mapped = set()
    for s_c, t_c in zip(s, t):
      if s_c not in stot:
        if t_c in t_mapped:
          return False
        stot[s_c] = t_c
        t_mapped.add(t_c)
      else:
        if t_c not in t_mapped or stot[s_c] != t_c:
          return False

    return True

