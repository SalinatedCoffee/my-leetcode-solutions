class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    # sorting with dictionary
    
    d = {n: i+1 for i, n in enumerate(sorted(set(arr)))}
    return map(d.get, arr)

