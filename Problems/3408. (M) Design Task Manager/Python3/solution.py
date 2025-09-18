class TaskManager:
  # min heap with dictionary
  def __init__(self, tasks: List[List[int]]):
    # populate internal heap and dictionary with elements in tasks
    self._task_heap = [(-p, -t, u) for u, t, p in tasks]
    heapify(self._task_heap)
    self._taskid_priorities = {t: (p, u) for u, t, p in tasks}

  def add(self, userId: int, taskId: int, priority: int) -> None:
    # push task onto heap and update dictionary
    heappush(self._task_heap, (-priority, -taskId, userId))
    self._taskid_priorities[taskId] = (priority, userId)

  def edit(self, taskId: int, newPriority: int) -> None:
    # retrieve original task, push modified task onto heap, and update dictionary
    userId = self._taskid_priorities[taskId][1]
    heappush(self._task_heap, (-newPriority, -taskId, userId))
    self._taskid_priorities[taskId] = (newPriority, userId)

  def rmv(self, taskId: int) -> None:
    # invalidate taskId in dictionary
    del self._taskid_priorities[taskId]

  def execTop(self) -> int:
    while self._task_heap:
      p, t, u = heappop(self._task_heap)
      # validate task on top of the queue by checking current priority & userId value of taskId against popped
      if -t in self._taskid_priorities:
        r_p, r_u = self._taskid_priorities[-t]
        # popped task is valid, invalidate taskId in dictionary before returning userId
        if -p == r_p and u == r_u:
          del self._taskid_priorities[-t]
          return u

    return -1

