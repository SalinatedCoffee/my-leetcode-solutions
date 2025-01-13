class Solution:
  def canConstruct(self, s: str, k: int) -> bool:
    # greedy algorithm using dictionary

    freq = Counter(s)
    odd = len(list(filter(lambda x: x[1] % 2 == 1, freq.items())))
    if k < odd:
      return False

    return True if len(s) >= k else False

