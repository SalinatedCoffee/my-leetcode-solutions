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

    # required number of matching pairs and currently matched
    pairs, matched = len(cnt_t), 0
    for c in cnt_t:
      if c in cnt_s and cnt_s[c] >= cnt_t[c]:
        matched += 1
    res = ""
    min_len = float('inf')
    i, j = 0, len(t)
    # s[:len(t)] and t already match, return early
    if pairs == matched:
      return s[:len(t)]
    while j < len(s):
      cnt_s[s[j]] += 1
      # if newly added character now matches
      if s[j] in cnt_t and cnt_s[s[j]] == cnt_t[s[j]]:
        matched += 1
      # try advancing i while substring matches
      while i <= j and matched == pairs:
        res = s[i:j+1] if j-i+1 < min_len else res
        min_len = min(min_len, j-i+1)
        cnt_s[s[i]] -= 1
        if s[i] in cnt_t and cnt_t[s[i]] > cnt_s[s[i]]:
          matched -= 1
        i += 1
      j += 1

    return res

