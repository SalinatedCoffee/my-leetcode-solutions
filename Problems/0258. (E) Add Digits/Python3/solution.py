class Solution:
  def addDigits(self, num: int) -> int:
    # iteration

    ret = 0
    while True:
      ret += num % 10
      num //= 10
      if not num:
        if ret < 10:
          break
        num = ret
        ret = 0
    
    return ret

