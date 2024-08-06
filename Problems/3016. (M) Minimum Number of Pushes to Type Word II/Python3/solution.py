class Solution:
  def minimumPushes(self, word: str) -> int:
    # greedy algorithm

    freq = sorted([(v, k) for k, v in Counter(word).items()], reverse=True)
    ret = 0
    for i, (v, _) in enumerate(freq):
      ret += (i // 8 + 1) * v

    return ret

