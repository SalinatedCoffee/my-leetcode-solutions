## 1615. (M) Maximal Network Rank

### `solution.py`
The 'network rank' of two different cities is defined as the sum of the number of roads connected to a pair of cities, where a road that directly connects the two cities should only be counted as 1 road. In other words, the rank is *almost* the sum of the degrees of each node in the pair, where we subtract 1 if the two nodes are directly connected. Since `n` is relatively small given the input constraints we can trivially solve this problem using brute force. We first generate an adjacency list where `adj[i]` is a set containing the neighboring nodes of `i`. Using a set allows us to perform 2 crucial operations in optimal time: checking the number of neighbors (the degree) and checking whether two nodes are connected by an edge. Now we simply compute the rank of all possible pairs of nodes and return the maximum rank.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is `n`. Generating `adj` can take $O(n^2)$ time, as well as the rank computation step for all node pairs. The space complexity is $O(n+m)$ where $m$ is the length of `roads`. `adj` is initialized as a list of empty sets of length $n$. `add()` is called twice for each road, thus the sets in `adj` will contain `2*len(roads)` items.  
  

### `solution_2.py`
We can try tweaking the previous solution to use lists instead of sets. Sets perform better than lists asymptotically, but has a much larger constant factor attached to them since there is a significant amount of overhead that comes from hashing. The one problem with using lists in a adjacency list is that it takes linear time to check whether a pair of nodes are connected or not. If we attempt to work around this problem by using an adjacency matrix, we now have no way of quickly checking the degree of a node. In order to make an adjacency matrix viable, we can store the degree of a node separately (stored in `adj[i][n]` in the solution).  
The solution logic is identical to the first solution.  

#### Conclusion
The time and space complexity is $O(n^2)$, but in practice this solution runs faster and uses less memory than the previous solution by virtue of using lists instead of sets.  
Perhaps a asymptotically better solution can be implemented by sorting the adjacency list by largest degree and greedily checking pairs.  