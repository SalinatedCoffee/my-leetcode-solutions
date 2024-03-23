class Solution:
  def intToRoman(self, num: int) -> str:
    # greedy

    tokens = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    r_nums = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    ret = ""
    idx = 0
    while num:
      # find largest 'token' smaller than remaining number
      while idx < len(tokens) and tokens[idx] > num:
        idx += 1
      num -= tokens[idx]
      ret += r_nums[idx]
    
    return ret

