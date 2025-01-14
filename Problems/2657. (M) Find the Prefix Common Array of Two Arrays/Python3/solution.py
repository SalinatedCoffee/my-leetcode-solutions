class Solution:
  def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
    # set

    n = len(A)
    freq = set()
    res, count = [], 0
    for i in range(n):
      if A[i] in freq:
        freq.remove(A[i])
        count += 1
      else:
        freq.add(A[i])
      if B[i] in freq:
        freq.remove(B[i])
        count += 1
      else:
        freq.add(B[i])
      res.append(count)

    return res

