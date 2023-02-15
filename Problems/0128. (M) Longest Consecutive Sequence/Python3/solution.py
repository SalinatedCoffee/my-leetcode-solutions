class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    # hash-based approach

    # cast elements into set
    nums_set = set(nums)
    max_len = 0
    for n in nums_set:
      # if n is smallest number in sequence
      if n-1 not in nums_set:
        i = n
        cur_len = 1
        # get length of sequence starting with n
        while True:
          i += 1
          if i not in nums_set:
            max_len = max(cur_len, max_len)
            break
          cur_len += 1
    
    return max_len

