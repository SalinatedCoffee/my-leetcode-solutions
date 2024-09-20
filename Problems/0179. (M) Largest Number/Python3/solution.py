class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    # sorting

    nums = list(map(lambda x: str(x), nums))
    nums.sort(reverse=True, key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
    # strip leading zeros
    res = ''.join(nums).lstrip('0')

    return res if len(res) else "0"

