## 1642. (M) Furthest Building You Can Reach

### `solution.py`
If we move to a building that is taller than the current building, we can either use a single ladder or multiple bricks proportional to the height difference to move to it. As we want to find the furthest building that we can move to using `ladders` ladders and `bricks` bricks, we would want to save the ladders to use on the largest height differences. This is, quite obviously, a greedy algorithm problem. As we iterate over `heights`, we prioritize the use of ladders until there are none left. Then, whenever we have to 'climb' to the next building, we greedily 'swap' the ladder used on the smallest height difference with bricks and use the now freed ladder on the current climb. When all ladders and bricks are exhausted, we return the index of the last visited building as we cannot move any further. If we simply store the ladder-climbed-heights in a list, we will have to scan through the entire list each time to determine the smallest value. We can instead store these values in a min heap, which trades constant time insertions / removals with constant time access to the smallest value.  

#### Conclusion
This solution has a time complexity of $O(n\log m)$, where $m$ is `ladders` and $n$ is the length of `heights`. As `heap` stores the height difference covered by each used ladder, it will at most store $m$ values. Insert / remove operations on a heap with $m$ values each take $O(\log m)$ time, which are performed at most twice for each element in `heights`. Thus, the overall time complexity is $O(n\log m)$. The space complexity is $O(m)$, as `heap` is the only object in memory that changes in size according to the input.  
  

