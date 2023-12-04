class Solution:
  def countCharacters(self, words: List[str], chars: str) -> int:
    # brute force using dictionaries

    bl_char = Counter(chars)
    
    def w_cmp(w):
      for c in w.keys():
        if c not in bl_char or w[c] > bl_char[c]:
          return False
      return True
    
    ret = 0
    for w in words:
      w_char = Counter(w)
      if w_cmp(w_char):
        ret += len(w)
    
    return ret

