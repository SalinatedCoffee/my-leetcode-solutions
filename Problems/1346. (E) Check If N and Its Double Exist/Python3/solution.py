class Solution:
  def checkIfExist(self, arr: List[int]) -> bool:
    # dictionary

    nums = Counter(arr)
    for num in arr:
      if nums[num*2] >= (2 if num == 0 else 1):
        return True

    return False

