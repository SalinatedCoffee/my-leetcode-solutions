## 2000. (E) Reverse Prefix of Word

### `solution.py`
Slicing in Python makes this problem almost trivial to solve. All we need to do is simply find the index of the first occurrence of `ch` in `word`, after which we reverse the prefix up to that index and contatenate it with the rest of `word`. If no occurrence of `ch` is found in `word` we return `word` as-is, as requested by the problem.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `word`. Scanning `word` for `ch`, as well as reversing the relevant prefix each take $O(n)$ time to perform. The space complexity is $O(1)$, excluding the memory required to store the string being returned.  
  

