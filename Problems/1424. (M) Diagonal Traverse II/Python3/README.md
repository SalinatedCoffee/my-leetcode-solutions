## 1424. (M) Diagonal Traverse II

### `TLE.py`
The most straightforward method is to simply traverse `nums` as described in the problem. As the length of the rows is not uniform however, we must first determine the length of the longest row. Once we have the 'dimensions' of `nums`, we can traverse the upper-left triangular region first and then the lower-right region to retrieve the values of `nums` in the desired order.  

#### Conclusion
This implementation has a time complexity of $O(n)$, where $n$ is the number of elements in `nums`. The space complexity is $O(m)$ where $m$ is the number of rows in `nums`.  
  

### `solution.py`
The first attempt fails with TLE, as it essentially tries to process empty cells that can be skipped. If `nums` is very sparse, or if one of its dimensions is disproportionally large/small compared to the other, the algorithm will waste a lot of time attempting to access nonexistent values in `nums`. Instead, we can iterate over only the existing values and later sort them based on their position in `nums`. If we examine the traversal order described in the problem, we can see that it is essentially asking us to 'fan out' from the origin. Thinking about `nums` as a lower-right quarter circle, we want to access the elements first by the 'radius' from the origin, and then in reverse order of their row numbers. An element's 'radius' from the origin can simply be computed by adding its row and column numbers. Elements inside the same diagonal will share the same radius, and for a group of elements we want to access them in reverse order of their row numbers.  
For every value in `nums`, we append a tuple containing the 'radius' and row number of the element. Once all values have been accounted for, we sort the list first by the radii, and then by the row numbers. Finally, we create the list of elements in `nums` using the sorted list and return it.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$. A tuple for every value in `nums` is stored in `vals`, which takes $O(n\log n)$ time to sort. Retrieving the elements of `nums` using `vals` takes $O(n)$ time, hence the overall time complexity of $O(n\log n)$. The space complexity is $O(n)$, as `vals` will use $O(n)$ memory.  
  

### `solution_2.py`
Instead of iterating over `nums` in an arbitrary fashion and sorting the results later, we can eliminate the sorting step by just traversing `nums` in the correct order. Combining the ideas from the TLE attempt and the first solution, we can iterate over `nums`, but group the elements based on their 'radii'. Because of this, we also have the added bonus of only having to ensure that we are accessing the elements by the correct row order. As previously mentioned, we want to access the elements in the same group in reverse order of their row numbers. Hence, we should be iterating over `nums` in reverse order as well.  
Starting from the last row of `nums`, we iterate along each row. We can determine the corresponding group of each element using its row and column number. Using this information, we simply append the value to the list containing the other elements in its group. Once all values in `nums` have been examined, we are left with a dictionary `rads` that contains lists of elements with the same radii. Starting with the first group with the radii of `0`, we concatenate all of the group lists in ascending order of their radii, after which we may return the constructed list.  

#### Conclusion
The time complexity of this solution is $O(n)$. Unlike the previous solution, this implementation eliminates the sorting step, leaving the traversal step and introducing a concatenation step. Both takes $O(n)$ time, and thus the overall time complexity is $O(n)$. The space complexity is still $O(n)$, as `rads` will contain every element in `nums`.  
  

### `solution_3.py`
We can further improve upon the previous solution by also considering the group number when iterating over `nums`. If we visualize the diagonals, we can see that it resembles a BFS traversal of a grid starting from the square with coordinates `[0, 0]`. In fact it *is* exactly BFS, using the [Manhattan distance](https://en.wikipedia.org/wiki/Distance#Other_spatial_distances) to determine the distance between a square and the origin.  
Initializing a deque `nodes` containing the origin square, we can implement an iterative BFS algorithm that traverses `nums` in the correct order. If we look at two adjacent diagonals, we can see that each square in the 'previous' diagonal only borders at most two squares in the next diagonal - one to the right and one below. There is only one case when a square in the previous diagonal borders a next square below it, and that is when the square is in the first column of `nums`.  
Starting at the first square at `nums[0][0]` (which is guaranteed to exist) we first append the value of the current node to a list, and then examine its coordinates. If it is in the first column, we enqueue the square below it (which is also guaranteed to exist) **first**. We then check if the square to its right exists, and enqueue that square if it does. As is usually the case for iterative BFS traversals, we continue until there are no nodes remaining in the queue. Once the traversal is completed, we simply return the list of values.  

#### Conclusion
This solution also has a time complexity of $O(n)$. BFS traverses each square in `nums` exactly once, taking $O(n)$ time overall. The space complexity is $O(\sqrt{n})$, because the deque `nodes` will at most contain all squares in the longest diagonal of `nums` - which is by definition, $O(\sqrt{n})$.  
  

