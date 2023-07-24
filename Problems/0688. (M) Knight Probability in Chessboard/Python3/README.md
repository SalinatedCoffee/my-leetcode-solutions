## 688. (M) Knight Probability in Chessboard

### `solution.py`
We can immediately identify that the probability as defined in the problem for a certain position depends on the probabilities of the knight at all possible next moves. This structure lends itself rather well to recursive solutions, and so we will be taking a top-down dynamic programming approach to the problem.  
At some square on the board there are 8 potential moves. Because moves are made randomly in uniform fashion, the probability from each move can be weighted equally. 8 potential moves, so we scale each probability by 1/8 = 0.125. We can now define a recursive function $f(r,c,s)$, which returns the probability when the knight is on the square with coordinates $(r, c)$ and has made $s$ moves. Then $f(r,c,s) = \sum_{moves=1}^{8}f(r_{moves},c_{moves},s+1)\times 0.125$. There are two base cases; if $(r, c)$ does not exist on the board, the return value is $0$, or if $(r, c)$ exists on the board and $s = \texttt{k}$ the return value is $1$.  
One detail that is easy to miss is that a move may bring the knight back to where it previously was, and as such we need to be able to differentiate between probabilities for different number of moves made - hence the 3D list used for memoization.  

#### Conclusion
This solution has a time complexity of $O(n^2k)$, where $n$ is `n` and $k$ is `k`. We use a 3D list `dp` with dimensions $n\times n\times k$, which takes $O(n^2k)$ time to initialize. The space complexity is also $O(n^2k)$ due to `dp` as mentioned earlier.  
Note that there are many possible optimizations that can be made to this solution - namely as the probability computation for `s` only depends on the values for the state `s-1`, the space complexity could be reduced to $O(n^2)$ by taking a bottom-up approach instead.  

