## 1496. (E) Path Crossing

### `solution.py`
Because we need to determine whether the current position has been traversed previously, we need to keep track of all of the coordinates that have been visited up to the current point in time. Since we do not know the range of the x and y coordinates of the path, and we want to quickly check whether a coordinate has been previously visited, the natural thing to do would be to use Python sets to store this information. This way we can insert and retrieve tuples in constant time without having to deal with resizing problems if we had used an array.  
We can simply insert a tuple of the x and y coordinates into a set, but we can make a small space optimization by using a dictionary with sets. If we were to move in a straight line, one coordinate would not change, and we would be storing the same integer multiple times. By using a dictionary that maps an x-coordinate to a set of y-coordinates, we can eliminate this redundancy with a little bit of overhead. `history` is a `defaultdict(set)` where `history[x]` is a set of y-coordinates that have been previously visited when the x-coordinate was `x`. We first update the current coordinate accordingly, and check if `x` exists in `history`, and `y` in `history[x]`. If so, we immediately return `True`. If not, we add `y` to `history[x]` (and `x` to `history` if necessary) and keep moving according to `path`. Once every step in `path` has been processed, we can finally return `False`.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `path`. Every step on `path` is examined exactly once, with each step taking constant time to process. The space complexity is also $O(n)$, since we store every step taken in `history`.  
  

