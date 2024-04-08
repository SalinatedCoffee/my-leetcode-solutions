class Solution:
  def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    # simulation

    queue = deque(students)
    s_idx = 0
    while queue:
      prev = len(queue)
      for i in range(len(queue)):
        student = queue.popleft()
        if student != sandwiches[s_idx]:
          queue.append(student)
        else:
          s_idx += 1
      # no students were served this round
      if prev == len(queue):
        return len(queue)

    return 0

