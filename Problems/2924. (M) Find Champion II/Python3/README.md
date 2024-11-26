## 2924. (M) Find Champion II

### `solution.py`
The relationship of `n` teams(with labels in the range `[0, n-1]`) is represented by a directed acyclic graph with the set of edges `edges`. A team is considered to be stronger than another team if there exists an edge in the graph from the team to another team. For example, the edge `0 -> 1` indicates that team `0` is stronger than team `1`. When these teams participate in a tournament, the champion of the tournament is the strongest team amongst all `n` teams. Given these conditions, we are asked to return the label of the champion team. If there are multiple potential champions, we are asked to return `-1`. Because we only want the champion team without the need to consider the relative power relationships across the different teams, we can simply scan through `edges` and filter out teams with a non-zero indegree. This can be easily accomplished by using a combination of Python's `Counter`s, list comprehension, and the `filter()` function. If the result contains more than 1 team, we return `-1` instead.  

#### Conclusion
This solution has a time complexity of $O(n + m)$, where $n$ is `n` and $m$ is the length of `edges`. The entirety of `edges` is examined to determine the indegree of each team, which takes $O(m)$ time to run. Teams that have a non-zero indegree are then filtered out of the list of indgrees, taking $O(n)$ time to complete. Thus, the overall time complexity of this solution is $O(n + m)$. The space complexity is $O(n)$.  
  

