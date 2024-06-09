class Solution:
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    # prefix sums

    ret = 0
    # prefix sum up to current element mod k
    prefixMod = 0
    # modGroups[i] is the number of subarrays where sum % k == i
    modGroups = [0] * k
    # intialize to 1 to account for when the entire array is valid
    modGroups[0] = 1

    for num in nums:
      # compute mod k of prefix sum
      prefixMod = (prefixMod + num) % k
      # count number of valid subarrays
      ret += modGroups[prefixMod]
      # increment number of subarrays where their sum mod k is prefixMod
      modGroups[prefixMod] += 1
    
    return ret

