class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    # simple iteration

    target = max(candies)
    
    return [c + extraCandies >= target for c in candies]

