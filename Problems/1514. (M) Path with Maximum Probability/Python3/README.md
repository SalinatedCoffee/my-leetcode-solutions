## 1514. M Path with Maximum Probability

### `solution.py`
Since we are given a weighted graph, and we want to optimize some value based on these weights, it seems as we can use Dijkstra's algorithm to solve this problem. The vanilla version of Dijkstra however finds the shortest weighted path, and we need to modify it slightly to fit the problem. At some node, the order in which the neighboring nodes are considered is now reversed because the largest weight is most optimal. Using the usual Python max heap hack, this can be easily implemented. Storing the maximum probabilities for each node in `probs`, we can skip traversing to a node through an edge if that path would result in a lower probability than what was already computed for that destination node. When either the priority queue of nodes is empty or node `end` has been reached, we are done. For the former, it means that there is no path between `start` and `end` so we return `0`. For the latter, we immediately return the associated probability since we traverse highest probability edges first, which guarantees that the first traversal to `end` will have the highest probability.  

#### Conclusion
This solution has a time complexity of $O(n+m\log n)$, where $m$ is the length of `edges` and $n$ is `n`. The space complexity is $O(m+n)$.  
  

