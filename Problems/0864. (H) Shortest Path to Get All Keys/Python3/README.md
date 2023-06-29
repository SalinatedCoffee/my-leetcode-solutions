## 864. (H) Shortest Path to Get All Keys

### `solution.py`
The problem is asking us to return the length of the shortest path, which gives us a hint as to which algorithm we should be using. Naturally we would want to use BFS but we are allowed to backtrack over already traversed cells, which is incompatible with standard BFS.  
Zooming out a little, we can see that the goal is to collect **all keys** and not unlocking all locks. Then, ignoring the locks, this simply means that we can perform BFS between all possible pairs of nodes in the set of key nodes and the start node, and select the path that traverses all nodes with the shortest length. If we factor the locks back in we know that we need to keep track of which keys we have picked up, since we need that information to determine whether a lock can be unlocked and whether we have collected all keys. We can represent a collection of keys with bit masks, where the keys are 0-indexed, and a `1` denoting that a key corresponding to that digit has been collected. For example, a state of `5` would mean that keys `a` and `c` have been collected (`5` in base 2 is `101`, where the LSB is `a`). Using these bitmasks we can mark a cell being visited in a certain state, which will allow us to retraverse it under a different state.  
When all keys have been collected, we can simply return the path distance of the current node. If the traversal completes without returning, it means that there is no possible path so we return the appropriate value of `-1`.  

#### Conclusion
The time complexity is $O(mn2^k)$, where $m$ and $n$ are the dimensions of `grid` and $k$ is the number of keys in `grid`. BFS touches all nodes in a graph once, and there can exist an instance of BFS for every possible key state, of which there are $2^k$ of. The space complexity is also $O(mn2^k)$.  
  

