## 1345. (H) Jump Game IV

### `TLE.py`
We can see that this problem can be translated rather nicely to a graph, where we would use BFS traversal since we want the least number of jumps (shortest path) to reach the last element. This can be trivially implemented - and this algorithm implements the iterative flavor of BFS.  
However, the algorithm is not fast enough on inputs where `arr` is long and contains mostly the same values.  

#### Conclusion
The time and space complexity is $O(n^2)$, where $n$ is the length of `arr`. This is because the worst case is when all values of `arr` are the same.  
  


### `solution.py`
The previous algorithm times out but is still correct, which tells us that with a few optimizations we hopefully can come up with an optimal solution. Taking the worst case example that was mentioned previously, we notice that we do not have to consider jumps between same values once that value has been processed. For example given an array `[1, 1, 1, 1]`, once we jump from index `0` and move on to index `1`, we can skip jumping to index `0` (and `2`, `3`) as those indices have already been added to `nodes` and is planned for traversal later. So, all we have to do is to simply avoid this redundant behavior which in this problem is implemented by deleting the key-value pair for the key `arr[i]` in dictionary `v2i`.  
  
#### Conclusion
This solution has a time and space complexity of $O(n)$, as we avoid re-traversing nodes which ensures that we move through an index exactly once.  
  
