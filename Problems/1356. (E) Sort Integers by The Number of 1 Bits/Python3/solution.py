class Solution:
  def sortByBits(self, arr: List[int]) -> List[int]:
    # 2-pass sorting
    
    arr.sort()
    arr.sort(key=lambda x: x.bit_count())
    
    return arr

