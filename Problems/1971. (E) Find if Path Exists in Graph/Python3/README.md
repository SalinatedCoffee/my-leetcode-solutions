## 1971. (E) Find if Path Exists in Graph

### `solution.py`
As the graph is undirected, we can simply traverse it with any traversal algorithm to determine whether `destination` is reachable from `source`. In this solution, we have chosen to implement the iterative flavor of DFS using a Python set to keep track of visited nodes.  
We first convert the list of edges `edges` to an adjacency list, after which we initialize an empty set and list containing `source` as its only element. Then, while the list of nodes `nodes` is not empty we pop the top item off of it and check whether if it has been already visited or if it is `destination`. For the former, we move on to the next node in `nodes`. For the latter, we immediately return `True` as we have reached `destination` starting at `source`. Otherwise, we go through the list of the current node's neighbors, pushing them onto the list (stack) of nodes to be visited in the future. If the traversal completes, it means that `destination` is not reachable from `source`, which also means that a path does not exist between the two nodes.  

#### Conclusion
This solution has a time complexity of $O(n^2)$ where $n$ is `n`. Converting `edges` to an adjacency list is a linear time operation. Since there can be at most $n(n+1)/2$ edges in an undirected graph with $n$ vertices, this step will take $O(n^2)$ time to complete. The DFS traversal has a time complexity of $O(|V|+|E|)$, where $V$ is the set of vertices and $E$ the set of edges in the graph being traversed. Hence, this becomes $O(n(n+1)/2 + n)$, which simplifies to $O(n^2)$. The space complexity is $O(n)$, due to `nodes` and `visited`.  
  

### `solution_2.py`
We can also solve this problem by using a data structure called union find(also known as disjoint-set), which groups nodes based on whether they are part of a connected component or not. In this problem, the given graph is undirected, hence a path is guaranteed to exist between two nodes if they are part of the same connected component. If two nodes are connected by an edge, they are part of the same connected component; so we merge the two connected components each node is a part of by calling `uunion`.  

#### Conclusion
The time complexity of this solution is $O(n^2)$. Operations on the union find data structure are considered to take $O(1)$ time. As we iterate over the list of edges `edges`, which length is $O(n^2)$, the overall time complexity becomes $O(n^2)$. The space complexity is $O(n)$, due to the list `p`.  
  

