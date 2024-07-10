class Solution:
  def minOperations(self, logs: List[str]) -> int:
    # simulated stack

    depth = 0
    for log in logs:
      if log == "../":
        depth -= 1 if depth else 0
      elif log != "./":
        depth += 1

    return depth

