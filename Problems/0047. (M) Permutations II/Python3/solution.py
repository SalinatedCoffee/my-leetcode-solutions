class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    # backtracking using hash maps

    n = len(nums)
    ret = []
    def recurse(cur, counts):
      if len(cur) == n:
        ret.append(cur[:])
      else:
        # select next available unique value
        for num in counts:
          if counts[num] > 0:
            cur.append(num)
            counts[num] -= 1
            recurse(cur, counts)
            cur.pop()
            counts[num] += 1
    
    recurse([], Counter(nums))

    return ret

