class Solution:
  def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    # bucket sort with greedy algorithm

    n = len(nums)
    # sanity check
    if n % k:
      return False
    
    # buckets[i] is number of elements in nums with value i
    buckets = Counter(nums)
    # for each unique value, in ascending order
    for key in sorted(buckets.keys()):
      # if non-zero number of elements remain
      if buckets[key]:
        # examine each consecutive value
        for i in range(key+1, key+k):
          # not able to match values, impossible to group nums
          if buckets[key] > buckets[i]:
            return False
          buckets[i] -= buckets[key]
        buckets[key] = 0

    return True

