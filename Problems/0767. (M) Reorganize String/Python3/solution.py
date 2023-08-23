class Solution:
  def reorganizeString(self, s: str) -> str:
    # max heap

    n = len(s)
    # count letters
    freq = Counter()
    for c in s:
      freq[c] += 1

    # convert to max heap
    freq = [(-1*freq[c], c) for c in freq]
    heapify(freq)

    # sanity check
    if -1*freq[0][0] > ceil(n / 2):
      return ""
      
    # generate rearranged string
    ret = [None] * n
    count, cur = heappop(freq)
    for i in range(0, n, 2):
      if not count:
        count, cur = heappop(freq)
      ret[i] = cur
      count += 1
    for i in range(1, n, 2):
      if not count:
        count, cur = heappop(freq)
      ret[i] = cur
      count += 1
    
    return "".join(ret)

