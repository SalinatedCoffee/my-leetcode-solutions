class Solution:
  def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    # sets

    whitelist = set(allowed)
    return len(list(filter(lambda x: set(x) <= whitelist, words)))

