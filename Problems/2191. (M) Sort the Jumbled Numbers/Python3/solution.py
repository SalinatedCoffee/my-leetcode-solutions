class Solution:
  def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
    # sort list using custom comparator

    # convert list of integers into single string
    map_str = ''.join(list(map(str, mapping)))
    # lambda function that converts an integer using mapping
    convert = lambda x: int(''.join(list(map(lambda i: map_str[int(i)], str(x)))))
    # sort nums using mapped values
    nums.sort(key=convert)
    
    return nums

