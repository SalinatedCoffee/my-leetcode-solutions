class Solution:
  def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
    # sorting with heap queues
    
    nums = list(zip(nums1, nums2))
    nums.sort(key=lambda x : x[1])
    selected = []
    max_score = 0
    select_sum = 0
    for i in range(len(nums)-1, -1, -1):
      if len(selected) < k:
        heappush(selected, nums[i][0])
        select_sum += nums[i][0]
        max_score = select_sum * nums[i][1]
      else:
        select_sum -= heapreplace(selected, nums[i][0])
        select_sum += nums[i][0]
        max_score = max(max_score, select_sum * nums[i][1])
    
    return max_score

