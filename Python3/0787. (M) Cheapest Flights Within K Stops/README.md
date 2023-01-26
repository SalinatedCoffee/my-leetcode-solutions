## 787. (M) Cheapest Flights Within K Stops

### `TLE.py`
A itinerary cannot have more stops than `k`. Thus, we may use BFS since it traverses through all nodes at a certain level before moving onto the next. This gives us the added optimization benefit of being able to exit the traversal early whenever the stops count exceeds `k`. For the return value, we only need to keep track of the minimum price of all previously traversed paths since we want the minimum cost of paths with steps in the interval `[0, k]`. However, this approach will time out on test cases where `n` is large since it tries all paths of length proportional to `k` starting at `src`.  

#### Conclusion
This algorithm runs in $O(n^2)$ time and uses $O(n)$ space, where $n$ is the number of nodes. 
  

### `solution.py`
We may optimize the previous algorithm further by realizing that we may prune paths early if the cost taken to reach a node from `src` is larger than the cost of a previous visit. To do this, we store the minimum costs in a list of length `n`. During traversal, we can move on to the next node in the queue early when the current cost is larger than `min_prices[current_node]`.  

#### Conclusion
The solution has a time complexity of $O(n^2)$ and a space complexity of $O(n)$. While the asymptotic time complexity is the same as the TLE algorithm, the early pruning optimization speeds up the practical runtime enough to pass all test cases.  
  

