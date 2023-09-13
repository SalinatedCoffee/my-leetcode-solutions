class Solution:
  def candy(self, ratings: List[int]) -> int:
    # greedy

    n = len(ratings)
    sweets = [1] * n

    for i in range(1, n):
      if ratings[i] > ratings[i-1]:
        sweets[i] = sweets[i-1]+1
    
    for i in range(n-2, -1, -1):
      if ratings[i] > ratings[i+1] and sweets[i] <= sweets[i+1]:
        sweets[i] = sweets[i+1]+1
    
    return sum(sweets)

