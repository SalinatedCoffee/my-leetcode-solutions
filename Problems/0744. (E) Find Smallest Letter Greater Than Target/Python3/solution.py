class Solution:
  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    # binary search
    
    lo, hi = 0, len(letters)-1
    while lo <= hi:
      mid = (hi + lo) // 2
      if letters[mid] > target:
        hi = mid-1
      else:
        lo = mid+1

    return letters[lo] if lo != len(letters) else letters[0]

