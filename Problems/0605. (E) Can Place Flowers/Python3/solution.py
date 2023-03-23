class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    # brute force (greedy)

    # sanity check
    if not n:
      return True

    fb = copy.deepcopy(flowerbed)
    planted = 0

    for i in range(len(fb)):
      if not fb[i]:
        # check left and right plots
        l = True if not i or not fb[i-1] else False
        r = True if i == len(fb) - 1 or not fb[i+1] else False
        # plant if plot available
        if l and r:
          fb[i] = 1
          planted += 1
          if planted >= n:
            return True
      
    return planted >= n

