class Solution:
  def numTeams(self, rating: List[int]) -> int:
    # brute force

    n = len(rating)
    ret = 0
    for i in range(n):
      # count elements strictly smaller/larger than current element in each side
      l_l, l_h = 0, 0
      r_l, r_h = 0, 0
      for j in range(i):
        if rating[j] < rating[i]:
          l_l += 1
        elif rating[j] > rating[i]:
          l_h += 1
      for j in range(i+1, n):
        if rating[j] < rating[i]:
          r_l += 1
        elif rating[j] > rating[i]:
          r_h += 1
      # compute number of selections
      ret += l_l * r_h
      ret += l_h * r_l

    return ret

