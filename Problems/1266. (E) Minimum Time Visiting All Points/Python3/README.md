## 1266. (E) Minimum Time Visiting All Points

### `solution.py`
We are asked to return the minimum travel distance to move between all points in `points`. Because the travel order is given to us, this is a very straightforward problem that can be solved by simply iterating over `points` and computing the minimum distance between two points. One peculiar aspect of this problem is that moving diagonally incurs the same cost as moving horizontally or vertically, despite the actual euclidean distance. Hence in order to minimize the travel distance between two points, it is optimal to go diagonally as often as we can. Given two points `(x1, y1)` and `(x2, y2)`, we calculate the difference on each axis and take the absolute value. This is the distance we would have to move on each axis to reach one point from the other. As previously mentioned, we want to move diagonally as much as possible. Moving diagonally will reduce the delta for both axes by 1. Thus, the number of diagonal moves that we can make will be bound by the smaller of the two differences. For the remainder of the journey we must travel either horizontally or vertically, which is simply the difference between the larger difference and smaller difference. Writing the expressions out, we have `dx, dy = abs(x1 - x2), abs(y1 - y2)`, `d = min(dx, dy) + (max(dx, dy) - min(dx, dy))`. The latter simplifies to `d = max(dx, dy)`.  
Now we simply need to iterate along `points` while computing the distance between the current and previous points. Once the loop exits we directly return the sum of all computed distances.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the length of `points`. The space complexity is $O(1)$.  
  

