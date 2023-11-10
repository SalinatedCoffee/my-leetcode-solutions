## 1743. (M) Restore the Array From Adjacent Pairs

### `solution.py`
Given an array of pairs of integers `adjacentPairs`, we are asked to reconstruct the original array `nums`. The pairs in `adjacentPairs` are (obviously) adjacent in the original `nums` array, and a pair `(i, j)` can exist in `nums` either as `[..., i, j, ...]` or `[..., j, i, ...]`. The values in `nums` are all unique.  
Because an answer is guaranteed to exist, and the original `nums` array only contains unique values, we can convert `adjacentPairs` into an undirected graph and simply traverse it to generate a path that traverses all nodes. Representing the graph as a adjacency list using a dictionary, the 'edge' nodes that exists on either end of `nums` will only have 1 neighbor instead of 2. We can use this property to start the graph traversal on a start/ending value, or we can simply start traversing from any pair and splice the resulting halves into a single list. Here we have chosen to implement the latter, using the iterative flavor of DFS to traverse the graph.  
One thing to remember is that when starting the traversal from each value of a pair, we must ignore the other value because the graph is undirected. This can be accomplished by simply adding the other value to the visited set before starting the traversal. Once the traversal finishes, we reverse one of the resulting lists and extend it with the other to reconstruct `nums`, which we can directly return.  

#### Conclusion
This solution has a time and space complexity of $O(n)$ where $n$ is the length of `adjacentPairs`. Generating the adjacency list and traversing the resulting graph both takes $O(n)$ time and uses $O(n)$ memory.  
  

