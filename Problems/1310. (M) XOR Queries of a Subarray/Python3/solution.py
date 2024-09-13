class Solution:
  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    # generate list of prefix XOR sums
    pre = [x for x in accumulate(arr, lambda x, y: x ^ y)]
    # append 0 to handle queries with a low of 0
    pre.append(0)
    
    return [pre[l-1]^pre[h] for l, h in queries]

