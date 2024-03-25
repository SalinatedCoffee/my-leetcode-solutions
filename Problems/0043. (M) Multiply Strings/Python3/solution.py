class Solution:
  def multiply(self, num1: str, num2: str) -> str:
    # long multiplication

    # convert char to integer
    ctoi = lambda x: ord(x) - ord('0')

    # convert first string to integer
    a = 0
    for num in num1:
      a += ctoi(num)
      a *= 10
    if a:
      a //= 10
    
    # perform multiplication
    prod = 0
    for i in range(len(num2)):
      t = a * ctoi(num2[-(i+1)])
      prod += t * 10**i
    
    # sanity check
    if prod == 0:
      return "0"

    # convert product back into string
    ret = ""
    while prod:
      ret += chr(ord('0') + prod % 10)
      prod //= 10

    return ret[::-1]

