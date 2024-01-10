## 2385. (M) Amount of Time for Binary Tree to Be Infected

### `solution.py`
Because the only requirement for a node to infect another node is for them to be adjacent to each other, we want to be able to freely traverse the tree since a child can infect its parent. The given tree makes this difficult as we cannot easily access the parent of a node. If we convert the tree into an undirected graph we can treat the tree as a generic graph, and run any traversal algorithm on it. The problem asks us to return the time it takes to infect all the nodes in the tree, where it takes 1 minute for a node to be infected. This is essentially asking us for the distance from the node `start` to the node farthest away from it(also called the diameter of the graph).  
We have opted to implement the iterative flavor of DFS for this problem, but any other traversal algorithm would work also. After an adjacency list is generated from the given tree, we traverse the tree starting at node `start`. The node and the distance from that node to `start` is pushed onto the stack as a tuple. Whenever an adjacent node is pushed onto the stack, the distance is incremented by `1`. Once the entire graph has been traversed, we simply return the largest distance in the graph from `start`.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the number of nodes in the tree rooted at `root`. Converting tree, and traversing the resulting graph both takes $O(n)$ time to perform. The space complexity is also $O(n)$ as the converted tree, set of visited nodes, and the DFS stack uses $O(n)$ memory each.  
Possible further optimizations would involve only generating edges from a node to its parent instead of all edges, as those from a node to its children would be redundant.  
  

