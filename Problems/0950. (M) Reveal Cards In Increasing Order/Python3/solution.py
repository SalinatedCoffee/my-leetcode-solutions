class Solution:
  def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    # simulate problem using queue

    n = len(deck)
    queue_idx = deque([i for i in range(n)])
    deck.sort()
    ret = [0] * n
    for card in deck:
      ret[queue_idx.popleft()] = card
      # pop and requeue
      queue_idx.rotate(-1)

    return ret

