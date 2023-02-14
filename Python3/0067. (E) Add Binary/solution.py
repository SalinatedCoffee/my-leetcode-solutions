class Solution:
  def addBinary(self, a: str, b: str) -> str:
    # walk both strings and construct result incrementally

    i, j, carry = len(a)-1, len(b)-1, 0
    ret = ''

    while i >= 0 or j >= 0:
      # add carry from previous sum
      total = carry
      # add digits from a and b if not oob
      total += 0 if i < 0 else ord(a[i])-ord('0')
      total += 0 if j < 0 else ord(b[j])-ord('0')
      # advance to next digit
      i -= 1
      j -= 1
      # append sum to digit
      ret += str(total%2)
      # carry over as necessary
      carry = total // 2
    
    # carry left over after addition
    if carry:
      ret += '1'
    
    # ret was constructed in reverse order
    return ret[::-1]

