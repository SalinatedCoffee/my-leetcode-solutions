## 46. (M) Permuations

### `solution.py`
This is another problem that can be solved by simple backtracking. We define a recursive function that takes two parameters; a list that contains the ordered choice of values in `nums` up to this point, and a set that contains the remaining values of `nums` that we can choose from. We iterate over the set of all possible selections, and for each element we add it to the list of selected values and remove it from the set of available choices, after which we make a recursive call with the new list and set as parameters. When the recursive call exists, we need to restore the state of the list and set for the next possible choice. The base case is when the list is the same length as `nums`, which indicates that all available values has been selected. When this happens, we simply append a copy of the current list to the return list and return immediately.  

#### Conclusion
This solution has a time complexity of $O(n\cdot n!)$ where $n$ is the length of `nums`. The number of permutations of $n$ elements is $n!$, and for each permuation we append a copy of it to `self.ret` which takes $O(n)$ time - hence the total running time of $O(n\cdot n!)$. The space complexity (excluding the returned object `self.ret`) is $O(n)$, since the recursion depth will be at most $n$.  
  

