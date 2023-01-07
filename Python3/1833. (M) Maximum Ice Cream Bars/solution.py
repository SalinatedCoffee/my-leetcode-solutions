class Solution:
  def maxIceCream(self, costs: List[int], coins: int) -> int:
    # always optimal to buy cheapest first
    # sorting cost list (nlogn) is cheaper that not sorting (n^2)

    costs.sort()
    purchased = 0

    for bar in costs:
      if coins >= bar:
        coins -= bar
        purchased += 1
      else:
        break

    return purchased

