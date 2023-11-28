## 935. (M) Knight Dialer

### `solution.py`
This problem can quite obviously be solved by using a dynamic programming approach, where the 2 state parameters are the position on the keypad and the number of digits to dial. As the same digit can be dialed multiple times, we memoize the return value of each state to avoid performing redundant computation. The base case is when there is only 1 digit left to dial, in which case we return `1`. Otherwise, we recurse on all valid moves that can be made from the current position and return the sum of all return values mod `10**9 + 7`.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is `n`. Each state has 2 parameters - the position on the keypad and the number of digits to dial. Because the keypad has a fixed size of 10, this means that we have $O(10n)$ states in total that we need to compute the values of. The computation that happens for each state takes $O(1)$ time to perform, hence the overall time complexity is $O(n)$. The $O(n)$ space complexity comes from the recursion stack, which can be at most $n$ deep.

#### `solution-optimized.py`
The original version takes a generalistic approach to the problem. As the keypad is small, and the number of possible moves from a digit is also small, we can simply predetermine the next digits for each digit and use that information when transitioning between states. For example, at position `(0,0)` (the key corresponding to 1) we can only move to `(1,2)` (the 6 key) or `(2,1)` (the 8 key). By doing so we can eliminate the boundary check step, which involves a handful of comparators and also has to deal with the 0 key explicitly. We can also reduce the dimensions down to 1, representing each key with a single integer instead of a tuple. Apart from the obvious computational savings, this also sets up the approach for the bottom-up dynamic programming solution.  
  

