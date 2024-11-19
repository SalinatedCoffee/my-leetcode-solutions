class Solution:
  def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    # dictionary with sliding window

    n = len(nums)
    # frequency of each unique element within current window
    w_nums = Counter(nums[:k])
    # sum of elements within current window
    w_sum = sum(nums[:k])
    res = w_sum if len(w_nums) == k else 0
    for i in range(k, n):
      # slide window and update its contents accordingly
      w_nums[nums[i]] += 1
      w_sum += nums[i]
      if w_nums[nums[i-k]] == 1:
        del w_nums[nums[i-k]]
      else:
        w_nums[nums[i-k]] -= 1
      w_sum -= nums[i-k]
      # try updating current max subarray length if window is valid
      if len(w_nums) == k:
        res = max(res, w_sum)

    return res

