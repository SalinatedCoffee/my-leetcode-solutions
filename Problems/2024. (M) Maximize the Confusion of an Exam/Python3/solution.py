class Solution:
  def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
    # sliding window

    n = len(answerKey)
    ret = -1
    for key in ['T', 'F']:
      l = 0
      tgts = 0
      for i in range(n):
        if answerKey[i] == key:
          tgts += 1
        while tgts > k:
          if answerKey[l] == key:
            tgts -= 1
          l += 1
        ret = max(ret, i - l + 1)
    
    return ret

