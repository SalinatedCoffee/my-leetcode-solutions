## 1220. (H) Count Vowels Permutation

### `solution.py`
Intuition tells us that we should try taking a dynamic programming approach to this problem. If we want to compute the number of ways to construct a vowel string of length `i` ending with vowel `v`, we would need the number of ways to construct a string of length `i-1` ending with whichever vowels can precede `v`. The direction of this recurrence relation requires us to transpose the permutation rules given in the problem, which is simple enough to work out.  
The recursive function only has 2 integer parameters, and is trivial to memoize. We want the number of ways to construct a vowel string of length `n`, which can end in *any* of the 5 vowels. Hence, we must return the sum of the results of `recurse(n, v)` for all vowels `v`.  

#### Conclusion
The time complexity of this solution is $O(nk) = O(n)$ where $n$ is `n` and `k` is the size of the vowels 'alphabet', which is a constant for this problem. Each state in the recurrence relation is represented by 2 integers, where one is bound by $n$ and the other by $k$. Computing the value of a single state takes constant time, and thus the overall time complexity comes out to be $O(n)$. The space complexity is also $O(n)$ since we keep the return value of all states in memory.  
  

