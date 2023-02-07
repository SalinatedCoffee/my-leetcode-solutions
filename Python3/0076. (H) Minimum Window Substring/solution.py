class Solution:
  def minWindow(self, s: str, t: str) -> str:
    # two pointers, try incrementing i whenever match is found
    #   break when window no longer matches

    # sanity check
    if len(s) < len(t):
      return ""

    # init letter freq.
    cnt_s = defaultdict(int)
    cnt_t = defaultdict(int)
    for i in range(len(t)):
      cnt_s[s[i]] += 1
      cnt_t[t[i]] += 1

    def compare(a, b):
      # a is letter freq of t
      # b is letter freq of window
      for c in a:
        if c not in b or a[c] > b[c]:
          return False
      return True
    
    res = ""
    min_len = float('inf')
    i, j = 0, len(t)
    while j < len(s):
      # match found
      if compare(cnt_t, cnt_s):
        # increment left-hand index
        while i < j:
          cnt_s[s[i]] -= 1
          prev = i
          i += 1
          # window no longer matches, revert and break
          if not compare(cnt_t, cnt_s):
            i = prev
            cnt_s[s[i]] += 1
            break
        # update substring and min length accordingly
        res = s[i:j] if j-i < min_len else res
        min_len = min(min_len, j-i)
      # advance right-hand index
      cnt_s[s[j]] += 1
      j += 1

    # check for substring ending in s[-1]
    if compare(cnt_t, cnt_s):
      while i < j:
        cnt_s[s[i]] -= 1
        prev = i
        i += 1
        if not compare(cnt_t, cnt_s):
          i = prev
          cnt_s[s[i]] += 1
          break
      res = s[i:j] if j-i < min_len else res

    return res

