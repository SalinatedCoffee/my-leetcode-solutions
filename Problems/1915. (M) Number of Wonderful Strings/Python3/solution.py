class Solution:
  def wonderfulSubstrings(self, word: str) -> int:
    # bit manipulation

    ret = 0
    mask = 0
    masks = Counter([mask])
    for c in word:
      # update mask with current letter
      mask ^= 1 << (ord(c) - ord('a'))
      # count mask that would yield all even substring
      ret += masks[mask]
      # update frequency of current mask
      masks[mask] += 1
      # find and count masks in prefix that differ by 1
      for i in range(10):
        ret += masks[mask ^ (1 << i)]

    return ret

