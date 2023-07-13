class Solution:
  def largestVariance(self, s: str) -> int:
    # kadane's algorithm

    freq = [0] * 26
    ctoi = lambda x: ord(x) - ord('a')
    for c in s:
      freq[ctoi(c)] += 1

    best_sum = 0
    for a in string.ascii_lowercase:
      for b in string.ascii_lowercase:
        if a == b or not freq[ctoi(a)] or not freq[ctoi(b)]:
          continue
        a_freq, b_freq = 0, 0
        b_rem = freq[ctoi(b)]
        for c in s:
          if c == a:
            a_freq += 1
          elif c == b:
            b_freq += 1
            b_rem -= 1
          if b_freq > 0:
            best_sum = max(best_sum, a_freq - b_freq)
          if a_freq - b_freq < 0 and b_rem > 0:
            a_freq, b_freq = 0, 0
    
    return best_sum

