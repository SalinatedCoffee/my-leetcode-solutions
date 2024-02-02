class Solution:
  def sequentialDigits(self, low: int, high: int) -> List[int]:
    # brute force

    # get number of digits in low
    d, t_low = 0, low
    while t_low:
      t_low //= 10
      d += 1

    ret = []
    while True:
      # construct starting value
      c, l = 0, 1
      for i in range(d-1, -1, -1):
        c += l * (10 ** i)
        l += 1
      # construct mask
      a = 0
      for i in range(d):
        a += 10 ** i
      # check every sequential number for current number of digits
      while c % 10 != 0:
        if low <= c <= high:
          ret.append(c)
        if c > high:
          return ret
        c += a
      d += 1

    return ret

