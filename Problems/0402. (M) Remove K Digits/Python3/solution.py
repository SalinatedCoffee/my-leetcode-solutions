class Solution:
  def removeKdigits(self, num: str, k: int) -> str:
    # increasing monotonic stack

    n = len(num)
    digits = []
    idx = 0
    while k and idx < n:
      # while budget allows, remove items in stack larger than current digit
      while k and digits and digits[-1] > num[idx]:
        digits.pop()
        k -= 1
      # add current digit if no budget, empty stack, or top of stack less than current
      digits.append(num[idx])
      idx += 1

    # reconstruct string after deletions
    ret = ''.join(digits) + num[idx:]
    # if budget not exhausted, greedily delete the larger digits
    if k:
      ret = ret[:-k]
    # truncate leading zeros
    l = 0
    while l < len(ret) and ret[l] == '0':
      l += 1

    # remember to return the string '0' if all digits deleted
    return ret[l:] if ret[l:] else '0'

