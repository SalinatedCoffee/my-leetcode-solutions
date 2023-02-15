## 1137. (E) N-th Tribonacci Number

### `solution.py`
A twist on the classic fibonacci number problem, this can be easily solved by memoizing previously computed values. We may use a list but here we're only interested in the n-th number, so we can save some space by only remembering the 3 most recently computed values.  
  
#### Conclusion
The solution runs in $O(n)$ time and uses $O(1)$ space.  
Even faster algorithms exist (at least for the fibonacci sequence) but they involve matrix multiplications which I'm pretty sure is out of the scope of this problem.  
  
