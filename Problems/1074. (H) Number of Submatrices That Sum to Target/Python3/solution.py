class Solution:
  def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    # prefix arrays with dictionaries

    m, n = len(matrix), len(matrix[0])
    # precalculate row prefix sum
    prefix = [[0]*n for _ in range(m)]
    for i in range(m):
      prefix[i][0] = matrix[i][0]
    for i in range(m):
      for j in range(1, n):
        prefix[i][j] = prefix[i][j-1] + matrix[i][j]
    
    ret = 0
    for i in range(n):
      for j in range(i+1):
        sums = defaultdict(int)
        sums[0] += 1
        cum_sum = 0
        for k in range(m):
          cum_sum += prefix[k][i] - (prefix[k][j-1] if j > 0 else 0)
          if cum_sum - target in sums:
            ret += sums[cum_sum - target]
          sums[cum_sum] += 1
    
    return ret

