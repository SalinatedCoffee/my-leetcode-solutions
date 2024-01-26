## 576. (M) Out of Boundary Paths

### `solution.py`
This is a very straightforward dynamic programming problem. Each state in the recurrence relation would need three parameters; the coordinates on the grid, and the number of remaining moves. We first check whether the current position is out of bounds or not. If it is, we simply return `1`. The remaining number of moves is examined next, where we return `0` if there are no moves remaining. If the current position is on the grid and there are remaining moves that can be made, we simply recurse on the four neighboring coordinates with the number of moves decreased by `1`. As the recurrence relation defines a function that accepts a coordinate and number of moves, then returns the number of ways to go out of bounds starting at that coordinate using that number of moves, the recursion should be started with `(startRow, startColumn, maxMoves)` as the arguments.  

#### Conclusion
This solution has a time complexity of $O(mnk)$, where $m$, $n$ and $k$ are `m`, `n`, and `maxMoves`, respectively. The states in the described recurrence relation have three parameters which are each bound by $m$, $n$, and $k$. We compute the return values for all possible states using $O(1)$ time for each state, hence the overall time complexity is $O(mnk)$. The space complexity is also $O(mnk)$, as the value of every state is memoized in memory.  
Implementing a bottom-up algorithm for this problem could be a good excercise as the dependency of a single state is not as straightforward as other problems (a hint would be to focus on the number of moves first).  
  

