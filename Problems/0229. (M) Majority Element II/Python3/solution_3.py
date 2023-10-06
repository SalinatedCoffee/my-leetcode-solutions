class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
    # constant space using Boyer-Moore majority vote algorithm
    # faster solution using built-in modules
    
    n = len(nums)
    maj = n // 3
    a, a_f, b, b_f = 0, 0, 1, 0
    for i in nums:
      if n == a:
        a_f += 1
      elif n == b:
        b_f += 1
      elif a_f == 0:
        a, a_f = n, 1
      elif b_f == 0:
        b, b_f = n, 1
      else:
        a_f -= 1
        b_f -= 1

    # list comprehension-specific if syntax
    return [x for x in [a, b] if nums.count(x) > maj]

