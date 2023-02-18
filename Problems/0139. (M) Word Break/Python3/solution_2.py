class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # optimized dp with sets

    # string is one character, just search directly
    if len(s) == 1:
      return s in wordDict

    words = set(wordDict)

    # value of dp[i] is whether s[0:i] is splittable
    dp = [False] * (len(s)+1)
    # empty string is always splittable
    dp[0] = True
    for i in range(1, len(s)+1):
      for j in range(i):
        # substring ending in previous char is splittable
        # and current substring of range [j, i] is in dictionary
        if dp[j] and s[j:i] in words:
          dp[i] = True
          # don't need to check for anything else, break early
          break

    return dp[-1]

