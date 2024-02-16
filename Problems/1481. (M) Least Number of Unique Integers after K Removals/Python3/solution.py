class Solution:
  def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    # greedy algorithm on sorted dictionary key-value pairs

    freq = sorted(Counter(arr).items(), key=lambda x: x[1])
    m, idx = len(freq), 0
    while idx < m:
      if freq[idx][1] > k:
        break
      k -= freq[idx][1]
      idx += 1

    return m - idx

