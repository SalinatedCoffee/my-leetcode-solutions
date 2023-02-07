class Solution:
  def totalFruit(self, fruits: List[int]) -> int:
    # dictionary-less single pointer solution

    max_picked = 0
    # types of picked fruit
    type_a, type_b = 0, 0
    # number of picked fruit b
    b_picked = 0
    picked = 0
    for fruit in fruits:
      # basket already exists for fruit
      if fruit in (type_a, type_b):
        picked += 1
      else:
        picked = b_picked + 1
      # fruit same as last picked
      if fruit == type_b:
        b_picked += 1
      else:
        b_picked = 1
        type_a, type_b = type_b, fruit
      max_picked = max(max_picked, picked)

    return max_picked

