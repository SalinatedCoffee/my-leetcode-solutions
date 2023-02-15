class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    # gcd property

    # sanity check
    if str1+str2 != str2+str1:
      return ""
    # gcd of strings exists, compute gcd
    gcd = math.gcd(len(str1), len(str2))
    
    # gcd-substring is prefix of either string of length gcd
    return str1[:gcd]

