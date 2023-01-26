class Solution:
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    prefixMod = 0
    res = 0
    # modGroups[i] contains number of subarrays where sum % k == i
    modGroups = [0] * k
    # intialize to 1 to account for entire array is valid
    modGroups[0] = 1

    for i, n in enumerate(nums):
      # compute mod k of prefix sum
      prefixMod = (prefixMod + n % k + k) % k
      # count number of valid subarrays
      res = res + modGroups[prefixMod]
      # increment number of subarrays where sum % k == pref. sum % k
      modGroups[prefixMod] += 1
    
    return res

