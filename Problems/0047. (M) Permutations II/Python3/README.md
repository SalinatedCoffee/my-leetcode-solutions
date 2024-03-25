## 47. (M) Permutations II

### `solution.py`
We are asked to return all *unique* permutations of `nums`. When choosing the next value to append to the current combination, we can avoid creating redundant combinations by only selecting a value from the remaining unique values from `nums`. This can be achieved by using a dictionary, where the key is the unique value and value the remaining number of that value in `nums`.  

#### Conclusion
The time complexity of this solution is $O(n\cdot n!)$ where $n$ is the length of `nums`. This is a loose upper bound, where we argue that generating a permutation takes $O(n)$ time and there are $O(n!)$ permutations in total, resulting in the overall time complexity of $O(n\cdot n!)$. A more tighter bound involves the summation of something called the [k-permutations of n](https://en.wikipedia.org/wiki/Permutation#k-permutations_of_n), which is explained in detail in the problem's [editorial](https://leetcode.com/problems/permutations-ii/editorial/). The space complexity is $O(n)$, as the dictionary can at most contain $n$ key-value pairs.  
  

