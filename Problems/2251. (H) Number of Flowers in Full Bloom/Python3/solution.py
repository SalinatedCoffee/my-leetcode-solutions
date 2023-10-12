class Solution:
  def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
    # binary search on sorted arrays
    
    n = len(flowers)
    # unzip flowers, then sort each list
    sf_s, sf_e = [], []
    for s, e in flowers:
      sf_s.append(s)
      sf_e.append(e)
    sf_s.sort()
    sf_e.sort()

    ret = []
    for p in people:
      s = bisect_right(sf_s, p)
      e = bisect_left(sf_e, p)
      ret.append(s - e)
    
    return ret

