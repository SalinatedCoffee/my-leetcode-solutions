class Solution:
  def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    # directly add num and k digit-by-digit

    k_int = k
    i, carry = len(num)-1, 0
    ret = []
    while i >= 0 or k_int:
      total = carry
      total += num[i] if i >= 0 else 0
      total += k_int % 10
      ret.append(total%10)
      carry = 1 if total >= 10 else 0
      i -= 1
      k_int //= 10

    if carry:
      ret.append(1)
    
    return ret[::-1]

