## 1547. (H) Minimum Cost to Cut a Stick

### `solution.py`
There is no optimal strategy to make a cut, and thus we cannot take a greedy approach to this problem. We can however use bottom-up dynamic programming where we consider the minimum cost to cut a portion of the stick. The positions of the available cuts can also serve as the interval range of stick fragments. For example if `cuts = [1, 4]` and `n = 6`, there can exist fragments of range `[0,1], [0,4], [0,6], [1,4], [1,6]...` and more. We can initialize a 2D list `dp`, where `dp[i][j]` contains the minimum cost to cut the stick fragment with the range `[i,j]`. Then, we can start filling in `dp` by first considering the intervals that have no cuts, then the intervals with one cut, and so on. Intervals that do not contain a cut will have a cost of `0`, since there is no cut that can be made. Borrowing the example from earlier, `dp[0][4]` will depend on the values `dp[0][1]` and `dp[1][4]`, and so on for all fragments that contain one available cut. Algorithmically, for every number of cuts `i` we iterate along `cuts`, trying every stick fragment with its leftmost cut at some element in it. Then we try all possible cuts between that leftmost cut `l` and `l+i`, while filling in `dp`.  
Once `dp` has been filled the desired value will be stored in `dp[0][-1]`, which we simply return.  
  
#### Conclusion
The time complexity of this problem is $O(n^3)$, where $n$ is the length of `cuts`. The upper-right 'triangle' of `dp` is computed, and there are $O(n^2)$ possible pairs of cuts. For each pair we try all possible cuts between them, which there are $O(n)$ of. The space complexity is $O(n^2)$ since `dp` has the dimensions $n+2 \times n+2$.  
  

