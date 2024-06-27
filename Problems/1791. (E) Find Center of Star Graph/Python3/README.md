## 1791. (E) Find Center of Star Graph

### `solution.py`
Given a 'star' graph with `n` nodes, where a node is connected with all other nodes by `n-1` edges, we are asked to return the value of the center node. Because the diameter of the given graph is always `3`, a non-center node will always have a degree of `1`. Thus, we can simply count the appearance of each node label in `edges` and return the one that appears the most number of times.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the graph. Because the length of `edges` is $n-1$, counting the node labels in `edges` will take $O(n)$ time. Finding the node label that appears most frequently will also take $O(n)$ time, bringing the overall time complexity to $O(n)$. The space complexity is also $O(n)$, due to the dictionary `freq`.  
  

### `solution-generic.py`
A more generic answer for star graphs with a diameter greater than 3 involves traversing the graph once to determine the diameter, and a second time to find the center node. Since the graph may have only 2 'arms', the counting approach of the previous solution cannot be used here. This is because in such a graph **all** nodes except the 'leaf' nodes at either end will have a degree of `2`. `edges` is first converted into an adjacency list to make it more easier to work with, after which an arbitrary leaf node is chosen as the origin. DFS is then performed starting at the origin, until another leaf node is found. At this point we know the diameter of the graph and in turn the radius. Starting at the arbitrary leaf node, we traverse the graph one last time in order to find the center node.  

#### Conclusion
The time and space complexity of this solution is $O(n)$.  