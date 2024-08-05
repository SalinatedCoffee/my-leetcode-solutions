class Solution:
  def kthDistinct(self, arr: List[str], k: int) -> str:
    # dictionary
    
    n = len(arr)
    # strs[w] is True if w is unique, False otherwise
    strs = {}
    for word in arr:
      if word not in strs:
        strs[word] = True
      else:
        strs[word] = False
    
    # Python dictionaries preserve insertion order
    # find and return k-th unique string by iterating over key-value pairs
    for word, v in strs.items():
      k -= 1 if v else 0
      if k == 0:
        return word

    return ""

