class Solution:
  def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    # simulated stack

    n = len(tickets)
    ret = 0
    idx = 0
    while tickets[k]:
      if tickets[idx]:
        tickets[idx] -= 1
        ret += 1
      idx += 1
      idx %= n

    return ret

