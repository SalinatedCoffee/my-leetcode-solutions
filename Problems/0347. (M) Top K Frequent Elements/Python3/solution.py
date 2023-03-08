class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # map values to frequency, then sort by frequency

    # done manually
    """
    counts = {}
    for n in nums:
      if n not in counts:
        counts[n] = 0
      counts[n] += 1
    
    tuples = []
    for n in counts:
      tuples.append((counts[n], n))
    tuples = sorted(tuples, reverse=True)

    return [tuples[x][1] for x in range(0, k)]
    """

    # done using builtins

    # subclass of dict, directly convert list to freq. dictionary
    counts = Counter(nums)

    # nlargest(n, iterable, key=None)
    # works since count.keys() is an iterable
    # key is function used to generate comparision value
    # counts.get is a function (.get() would be a call to that function)
    return heapq.nlargest(k, counts.keys(), key=counts.get)

