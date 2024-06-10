class Solution:
  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    # bucket sort with greedy algorithm

    n = len(hand)
    # sanity check
    if n % groupSize:
      return False
    
    # buckets[i] is number of remaining cards with value i
    buckets = Counter(hand)
    for i in sorted(buckets.keys()):
      # for each card value, greedily match against consecutive cards in its group
      if buckets[i]:
        for j in range(i+1, i+groupSize):
          # not enough cards to be matched, deck is impossible to group
          if buckets[i] > buckets[j]:
            return False
          # otherwise, greedily match cards
          buckets[j] -= buckets[i]
        # if this line is reached, all cards with value i have been matched
        buckets[i] = 0

    return True

