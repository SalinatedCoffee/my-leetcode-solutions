class Solution:
  def totalFruit(self, fruits: List[int]) -> int:
    # keep track of which fruits have been picked
    # two pointers

    # type and number of picked fruits
    baskets = {fruits[0]:1}
    max_picked = 1
    i, j = 0, 1
    while j < len(fruits):
      # basket already exists for rightmost fruit
      if fruits[j] in baskets:
        baskets[fruits[j]] += 1
        max_picked = max(max_picked, sum(baskets.values()))
      else:
        # only using one basket
        if len(baskets) < 2:
          baskets[fruits[j]] = 1
          max_picked += 1
        # already using two baskets
        else:
          baskets[fruits[j]] = 1
          # increment left pointer until one basket is emptied
          while i < j:
            baskets[fruits[i]] -= 1
            if baskets[fruits[i]] == 0:
              del baskets[fruits[i]]
              i += 1
              break
            i += 1
      j += 1

    return max_picked

