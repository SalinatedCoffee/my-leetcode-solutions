class Solution:
  def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    # greedy
    
    seats.sort()
    students.sort()
    ret = 0
    for i, j in zip(seats, students):
      ret += abs(i - j)

    return ret

