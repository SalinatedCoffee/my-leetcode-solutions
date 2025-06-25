class Solution:
  def maxDiff(self, num: int) -> int:
    # greedy

    # explode num into list of its digits
    digits = []
    while num:
      digits.append(num % 10)
      num //= 10
    digits.reverse()

    # helper function that concatenates list of digits into single integer
    def digits_to_int(nums):
      ret = 0
      for i in range(len(nums)):
        ret *= 10
        ret += nums[i]
      return ret
    
    # greedily apply operation to determine the largest possible value
    tgt = -1
    for d in digits:
      if d != 9:
        tgt = d
        break
    t = digits[:]
    if tgt != -1:
      t = list(map(lambda x: x if x != tgt else 9, t))
    a = digits_to_int(t)

    # greedily apply operation to determine the smallest possible value
    i = 0
    while i < len(digits) and digits[i] <= 1:
      i += 1
    t = digits[:]
    if i < len(digits):
      sub = 0 if i > 0 else 1
      tgt = digits[i]
      t = list(map(lambda x: x if x != tgt else sub, t))
    b = digits_to_int(t)

    return a - b

