class Solution:
  def convertToTitle(self, columnNumber: int) -> str:
    # base 26 modulo
    
    ret = ""
    while columnNumber:
      r, columnNumber = columnNumber % 26, columnNumber // 26
      if not r and columnNumber:
        columnNumber -= 1
        ret = 'Z' + ret
      else:
        ret = chr(r-1+ord('A')) + ret

    return ret

