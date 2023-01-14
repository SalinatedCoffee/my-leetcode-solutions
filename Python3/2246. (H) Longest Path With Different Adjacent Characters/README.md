## 2246. (H) Longest Path With Different Adjacent Characters

### `solution.py`
Another day, another tree problem. We want the length of the longest path, so we can use DFS. Before we begin let's first make sure that what a path actually is - according to Wikipedia, in graph theory a path "[is a finite or infinite sequence of edges which joins a sequence of vertices which, by most definitions, are all distinct](https://en.wikipedia.org/wiki/Path_(graph_theory))". By consequence this means that at a node, there cannot be a path that spans more than two subtrees (this is important since we're given n-ary trees as input, rather than a binary tree).  
Now we can start implementing a solution, and we're starting things off by constructing an adjacency list for easier access to the tree during traversal. For the recursion we have three things to keep in mind; first, the longest path may not go through the root. Second, if there are more than two valid subtrees we have to choose the 2 longest paths. And finally, even if we have multiple valid subtrees when we ascend a recursion level we can only use the longest path since a valid path cannot have any branches. Once we have these important points down the actual implementation is rather easy as shown in the solution.  
  
#### Conclusion
This solution runs in $O(n)$ time where $n$ is the number of nodes. The space complexity is $O(n + E)$ where $E$ is the number of edges, since we keep an adjacency list in memory.  
  
