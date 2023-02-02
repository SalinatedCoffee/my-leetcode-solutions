class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    # remember subsequences, 'overwrite' previous as necessary
    # binary search to find insertion index

    # length of LIS is at least 1
    subseq = [nums[0]]

    for i in nums:
      # current is larger than last item in memoized subseq.
      if i > subseq[-1]:
        # add item to end of subseq.
        subseq.append(i)
      elif i < subseq[-1]:
        # find smallest item that is larger than current, replace
        subseq[bisect.bisect_left(subseq, i)] = i
    
    return len(subseq)

