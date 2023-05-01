class Solution:
  def average(self, salary: List[int]) -> float:
    # sort

    salary.sort()

    return sum(salary[1:-1]) / (len(salary)-2)

