class Solution:
  def numTeams(self, rating: List[int]) -> int:
    # Fenwick (binary indexed) tree

    n = len(rating)
    max_rating = max(rating)
    # trees containing elements to either side of current element
    l_tree, r_tree = [0]*(max_rating+1), [0]*(max_rating+1)

    # increments the frequency of idx by val in tree tree
    def update(tree, idx, val):
      while idx < len(tree):
        tree[idx] += val
        idx += idx & (-idx)
    
    # returns frequency of all elements less than or equal to idx
    def prefix_sum(tree, idx):
      ret = 0
      while idx > 0:
        ret += tree[idx]
        idx -= idx & (-idx)
      return ret
    
    # initialize right side tree
    for rate in rating:
      update(r_tree, rate, 1)
    
    ret = 0
    for i in range(n):
      # exclude current element from right side tree
      rate = rating[i]
      update(r_tree, rate, -1)

      # retrieve appropriate frequencies from either side of current element
      l_l = prefix_sum(l_tree, rate-1)
      r_l = prefix_sum(r_tree, rate-1)
      l_h = i - prefix_sum(l_tree, rate)
      r_h = n - i - 1 - prefix_sum(r_tree, rate)

      # compute and add number of valid selections
      ret += l_l * r_h
      ret += l_h * r_l

      # add current element to left side tree
      update(l_tree, rate, 1)

    return ret

