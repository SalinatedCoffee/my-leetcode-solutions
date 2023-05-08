class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    # sliding window

    cur = 0
    vowels = "aeiou"
    for i in range(k):
      if s[i] in vowels:
        cur += 1

    ret = cur
    for i in range(k, len(s)):
      if s[i-k] in vowels:
        cur -= 1
      if s[i] in vowels:
        cur += 1
      ret = max(ret, cur)

    return ret

