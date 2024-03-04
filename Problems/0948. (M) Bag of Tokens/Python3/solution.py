class Solution:
  def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    # greedy algorithm on sorted list

    n = len(tokens)
    # sanity check
    if n == 0:
      return 0

    l, r = 0, n-1
    tokens.sort()
    ret = 0
    while l < r:
      # have enough power to score
      if power >= tokens[l]:
        ret += 1
        power -= tokens[l]
        l += 1
      # have enough score to increase power
      elif ret:
        ret -= 1
        power += tokens[r]
        r -= 1
      # can no longer play
      else:
        return ret

    # check last token before returning score
    return ret + (1 if power >= tokens[l] else 0)

