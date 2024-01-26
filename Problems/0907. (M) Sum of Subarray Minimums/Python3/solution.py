class Solution:
  def sumSubarrayMins(self, arr: List[int]) -> int:
    # monotonic stacks

    n = len(arr)

    def populate(left = True):
      # return list of indices generated using monotonic stack
      params = [n] if left else [n-1, -1, -1]
      pre = [-1] * n if left else [n] * n
      stack = []
      for i in range(*params):
        while stack and arr[stack[-1]] >= arr[i]:
          if left is False and arr[stack[-1]] == arr[i]:
            break
          stack.pop()
        if stack:
          pre[i] = stack[-1]
        stack.append(i)

      return pre

    ret = 0
    # left[i] contains index of first element smaller than arr[i] to its left
    # and vice versa
    left, right = populate(), populate(False)
    for i in range(n):
      # compute number of subarrays with minimum value arr[i]
      ret += (i - left[i]) * (right[i] - i) * arr[i]

    return ret % (10**9 + 7)

