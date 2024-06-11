class Solution:
  def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    # count elements using dictionary
    
    arr1_freq = Counter(arr1)
    ret = []
    # construct partial sorted array based on ordering of arr2
    for num in arr2:
      ret.extend([num]*arr1_freq[num])
      del arr1_freq[num]
    
    # add elements of arr1 not in arr2 to sorted list
    for num in sorted(arr1_freq.keys()):
      ret.extend([num]*arr1_freq[num])

    return ret

