## 1799. (H) Maximize Score After N Operations

### `solution.py`

The crux of this problem is that we need to try all possible pairs, since there is no (obvious) way that we could use GCD to our advantage. For this solution, we will be utilizing top-down DP with bitmasking to denote values in `nums` that have already been used. The benefit of using bitmasks instead of some other generic data structure is that we can keep the states compact (single integer per state) while keeping read / write operations reasonably fast. Our recursive function will take two values; the state bitmask as an integer, and the number of pairs that have been already selected. At a recursive call we will select a pair of integers that have not been selected and recurse on the remaining integers, and update the maximum score accordingly. After trying all possible pairs in this fashion, we finally update the score for this state in `memo` and return it.  

In this configuration, the value we want is the return value of `recurse(0, 0)` which denotes the state where we have no pairs selected.  

#### Conclusion

This solution has a time complexity of $O(4^nn^2\log k)$ where $n$ is half the length of `nums` and $k$ is the largest number in `nums`. There are $2^{2n}$ possible states, and for each state we check all other possible pairs, which takes $O(n^2)$ time. For each pair we compute the GCD which scales with the magnitude of the input values, hence the worst case running time of $O(\log k)$. The space complexity is $O(4^n)$ because the recursion stack will at most be $n$ deep, and `memo` will contain scores for each possible state, which there are $2^{2n}$ of.  


