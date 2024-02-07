class Solution:
  def frequencySort(self, s: str) -> str:
    # dictionary with sorting

    freq = Counter(s)
    freq = list(freq.items())
    freq.sort(key=lambda x: x[1], reverse=True)
    ret = ""
    for c, f in freq:
      ret += c * f

    return ret

