class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    # slow/fast pointers

    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
      slow = nums[slow]
      fast = nums[nums[fast]]

    finder = 0
    while slow != finder:
      slow = nums[slow]
      finder = nums[finder]
    
    return slow

