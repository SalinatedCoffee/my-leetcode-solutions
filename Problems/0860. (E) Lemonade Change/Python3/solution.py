class Solution:
  def lemonadeChange(self, bills: List[int]) -> bool:
    # greedy algorithm

    a, b = 0, 0
    for i in bills:
      match i:
        case 5:
          a += 1
        case 10:
          if a == 0:
            return False
          a -= 1
          b += 1
        case 20:
          if a and b:
            a -= 1
            b -= 1
          elif a > 2:
            a -= 3
          else:
            return False

    return True

