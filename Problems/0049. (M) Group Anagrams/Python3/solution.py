class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # dictionary with string compression
    
    n = len(strs)
    groups = defaultdict(list)
    for s in strs:
      freq = [0] * 26
      for c in s:
        # save a few CPU cycles by using ASCII code directly instead of ord('a')
        freq[ord(c) - 97] += 1
      cmpr = ""
      for i in range(26):
        if freq[i]:
          cmpr += f"{chr(i + 97)}{freq[i]}"
      groups[cmpr].append(s)

    return [i for i in groups.values()]

