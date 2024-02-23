## 787. (M) Cheapest Flights Within K Stops

### `TLE.py`
A itinerary cannot have more stops than `k`. Thus, we may use BFS since it traverses through all nodes at a certain level before moving onto the next. This gives us the added optimization benefit of being able to exit the traversal early whenever the stops count exceeds `k`. For the return value, we only need to keep track of the minimum price of all previously traversed paths since we want the minimum cost of paths with steps in the interval `[0, k]`. However, this approach will time out on test cases where `n` is large since it tries all paths of length proportional to `k` starting at `src`.  

#### Conclusion
This algorithm runs in $O(n^2)$ time and uses $O(n)$ space, where $n$ is the number of nodes. 
  

### `solution.py`
We may optimize the previous algorithm further by realizing that we may prune paths early if the cost taken to reach a node from `src` is larger than the cost of a previous visit. To do this, we store the minimum costs in a list of length `n`. During traversal, we can move on to the next node in the queue early when the current cost is larger than `min_prices[current_node]`. This is exactly [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), slightly modified to omit information about the previous node as we are only interested in the total weight of a path.  

#### Conclusion
The solution has a time complexity of $O(n^2)$ and a space complexity of $O(n)$. While the asymptotic time complexity is the same as the TLE algorithm, the early pruning optimization speeds up the practical runtime enough to pass all test cases.  
  

### `solution_2.py`
We can reduce the time complexity further by implementing Dijkstra's algorithm with a priority queue instead. This will allow us to always examine the shortest path first, without having to traverse all available paths between the source and destination nodes. The overall idea is similar; we push a triple containing the total distance (cost) of the path taken up to the current node, the number of 'hops' made, and the current node itself into a min heap. The min heap will guarantee that the first element will represent the shortest path being traversed. `dist[i]` now stores the number of hops in the shortest path between `src` and `i` instead of the actual distance. After an item is popped off of the heap, we first check the number of hops. If it is larger than `k+1`, the current path is not viable, and we skip to the next item on the heap. Then we check if the current node is `dst`. As previously mentioned, using a min heap guarantees that paths will be considered in order of their lengths; thus it is also guaranteed that the first path that reaches `dst` will be the shortest possible. If `cur == dst`, we simply return the length of the current path. The next conditional `if dist[cur] == h` is not as obvious, but also not that difficult to reason about. Since we know that we are considering paths in ascending order of their lengths, reaching a previously traversed node using the exact number of hops as the previous path will mean that the current path is longer than the previous one. Hence in this case, we simply skip to the next element on the heap. Finally, we examine all neighbors of the current node, pushing a neighbor onto the heap only if it has not been traversed or its previous path had more hops than the current path.  
If the outer while loop exits normally, it means that there were no viable paths from `src` to `dst`, so we return `-1` as requested by the problem.  

#### Conclusion
The time complexity is $O(n\log n)$, and the space complexity is $O(n)$.  