## 1688. (E) Count of Matches in Tournament

### `solution.py`
The easiest approach would be to simply simulate the tournament. We first check if `n` is odd. Then we halve `n`, truncating the result into an integer. After we add `n` to the number of matches `ret`, we add `1` if `n` was odd before the halving. These steps are then continued until `n` becomes `1`.  

#### Conclusion
This solution has a time complexity of $O(\log n)$, where $n$ is `n`. Each iteration halves `n`, and during each iteration we perform a handful of operations that take constant time. The space complexity is $O(1)$.  
  


### `solution_2.py`
If we think about this problem further, we realize that the tournament going on until 1 winning team remains also means that `n - 1` teams will be eliminated. Because a match *must* result in a winner and a loser, we can say that one team will be eliminated for each and every match that will be played. Hence, we can simply return `n - 1` directly instead of simulating the tournament.  

#### Conclusion
The time and space complexity of this problem is $O(1)$.  
  

