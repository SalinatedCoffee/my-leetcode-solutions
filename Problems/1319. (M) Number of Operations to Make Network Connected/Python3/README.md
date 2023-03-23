## 1319. (M) Number of Operations to Make Network Connected

### `solution.py`
We first need to identify how the minimum number of reconnections can be determined. At the most basic level, there needs to be at least one cable connecting two disconnected components, across all of them. That is, if we have `n` components, we will need `n-1` cables to connect them. We may exit early if the number of cables is less than the number of computers - 1. If there are `k` cables (where `k >= n-1`) and there are `m` disconnected components, that would mean that there are `k-(m-1)` redundant connections that are available to us. We have already established that we require *at least* `n-1` edges to connect `n` disconnected components, and so the smallest number of reconnections is exactly the number of disconnected components.  
To count the number of the disconnected components then, we may use union-find.

#### Conclusion
This solution has a time complexity of $O(m)$ where $m$ is the number of connections. Union-find merge operations are considered to have a practically constant running time, which is performed for every connection in `connections`.
The space complexity is $O(n)$ where n is the number of computers, since the `parent` of each computer is stored in a list of length $n$.
  


### `solution_2.py`
The basic idea is the same as the first solution, but we can also determine the number of disconnected components by doing a DFS traversal on the provided network of computers. By initiating DFS from every computer while sharing the *same visited set* of nodes, the number of disconnected components can be trivially counted.  

#### Conclusion
The time complexity is $O(n+m)$ since this solution essentially runs DFS 'incrementally' over the entire network. The space complexity is $O(m)$.  
  

