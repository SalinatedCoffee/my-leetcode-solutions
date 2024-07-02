class Solution:
  def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:

    hours[0] = 1 if hours[0] >= target else 0
    return reduce(lambda x, y: x + (1 if y >= target else 0), hours)

