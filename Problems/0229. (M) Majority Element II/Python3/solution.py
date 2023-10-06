class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
    # linear time and space using dictionary
    
    n = len(nums)
    maj = n // 3
    freq = Counter(nums)
    ret = []
    for k in freq.keys():
      if freq[k] > maj:
        ret.append(k)
  
    return ret

