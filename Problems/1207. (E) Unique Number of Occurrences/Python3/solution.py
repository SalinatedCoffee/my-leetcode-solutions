class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    # brute force using hash maps

    freq = Counter(arr)
    freq_set = set(freq.values())

    return len(freq.keys()) == len(freq_set)

