## 1043. (M) Partition Array for Maximum Sum

### `solution.py`
This is clearly a dynamic programming problem, since we can trivially compute the maximum sum of creating the partition `arr[i:j]` if we know the maximum sum of partitioning `arr[i+j:]`.  
Our recurrence relation will have a single parameter `idx`, which will denote the position within `arr` that is currently being considered. At `arr[idx]` then, we can try creating all possible partitions starting at index `idx`, of which there are `k` of. Since we want to maximize the sum, we choose the partition that yields the largest value. By how the recurrence relation was defined, we want the return value of `recurse(0)`, which we can return directly.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the length of `arr`. Each state in the recurrence relation is represented by a single integer which is bound by $n$. We compute the value for every possible state, with each computation taking $O(n)$ time to complete. Hence the overall time complexity is $O(n)$. The space complexity is also $O(n)$, as the values of all states are memoized in memory. The recursion stack can also be at most $n$ tall.  
  

