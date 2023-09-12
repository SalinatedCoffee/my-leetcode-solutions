class Solution:
  def minDeletions(self, s: str) -> int:
    # greedy
    
    # count frequencies
    freq = [0] * 26
    for c in s:
      freq[ord(c) - ord('a')] += 1

    # delete characters
    ret = 0
    for i in range(26):
      while freq[i] != 0 and (freq[i] in freq[i+1:] or freq[i] in freq[:i]):
        freq[i] -= 1
        ret += 1

    return ret

