## 2849. (M) Determine if a Cell Is Reachable at a Given Time

### `solution.py`
Given 2 points on an infinite 2D grid, we want to determine whether the square at coordinates `(fx, fy)` is reachable after exactly `t` seconds from the square at `(sx, sy)`. We are *forced* to move after every second, but can revisit squares as much times as we want. At each square we can move to any of its 8 adjacent neighbors. Obviously, we cannot reach the finish square if we are given less time than the time it takes to traverse the shortest path from the start to finish. How do we compute the distance between two squares then? Because we can also move diagonally, we can visualize the distance increasing by `1` as the ring of squares 'radiate' further outwards from the site of impact. This type of distance metric is called the [Chebyshev distance](https://en.wikipedia.org/wiki/Chebyshev_distance), and can be computed by taking the maximum of the difference between the x and y coordinates. If `t` is less than the distance between `(sx, sy)` and `(fx, fy)`, we simply return `False`, and `True` otherwise.  
There is however, one edge case that we need to consider. If the start and finish squares are the same, we can only be on the finish square when the given time is **not** `1`. This is because we are *required* to move every `1` second, and once we move off of the finish square, we cannon return to it when we are only given `1` second.  

#### Conclusion
The time and space complexity for this solution is $O(1)$.  
  

