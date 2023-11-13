class Solution:
  def sortVowels(self, s: str) -> str:
    # sorting

    n = len(s)
    # use a set for a small performance gain
    vowels = set([c for c in "aeiouAEIOU"])
    s_list = [None] * n

    # extract vowels and sort by ASCII code
    v_list = []
    for c in s:
      if c in vowels:
        v_list.append(c)
    v_list.sort(key=lambda x: ord(x))

    # reconstruct string with sorted vowels
    # iterate along s and v_list in parallel
    v_idx = 0
    for i in range(n):
      if s[i] in vowels:
        s_list[i] = v_list[v_idx]
        v_idx += 1
      else:
        s_list[i] = s[i]

    return ''.join(s_list)

