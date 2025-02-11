class Solution:
  def removeOccurrences(self, s: str, part: str) -> str:
    # KMP algorithm

    m, n = len(part), len(s)
    # compute LPS values for part
    lps = [0] * m
    idx, pre_len = 1, 0
    while idx < m:
      if part[idx] == part[pre_len]:
        pre_len += 1
        lps[idx] = pre_len
        idx += 1
      elif pre_len:
        pre_len = lps[pre_len-1]
      else:
        lps[idx] = 0
        idx += 1

    # match part against s
    stack = []
    idxs = [0] * (n+1)
    s_idx, idx = 0, 0
    while s_idx < n:
      stack.append(s[s_idx])
      if s[s_idx] == part[idx]:
        idx += 1
        idxs[len(stack)] = idx
        # match found, remove matching characters from stack
        if idx == m:
          for _ in range(m):
            stack.pop()
          idx = 0 if not stack else idxs[len(stack)]
      else:
        if idx:
          idx = lps[idx - 1]
          s_idx -= 1
          stack.pop()
        else:
          idxs[len(stack)] = 0
      s_idx += 1
    
    return ''.join(stack)

