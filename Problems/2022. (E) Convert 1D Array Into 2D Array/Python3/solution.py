class Solution:
  def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
    # list slices
    
    return [] if len(original) % n or m*n != len(original) else [original[i*n:(i+1)*n] for i in range(len(original) // n)]

