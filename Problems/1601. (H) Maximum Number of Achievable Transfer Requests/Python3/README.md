## 1601. (H) Maximum Number of Achievable Transfer Requests

### `solution.py`  
Because there is no subproblem that this problem can be simplified to, and the input size of `requests` is very small, we can try taking a brute force approach and simply try all possible combinations of granted requests. Here we will be taking a recursive backtracking approach. We keep track of the employee number change for each buildings, and try recursing after granting the current request, and after not granting the current request. Whenever the last request has been processed (which is different than it being granted) we check the number changes and see if any of them are not `0`. If yes, we can simply return as we have reached an invalid grant combination. If no, we update `self.ret` accordingly.  

#### Conclusion
This solution has a time complexity of $O(2^mn)$ where $m$ is the length of `requests` and $n$ is `n`. There are $2^m$ possible grant combinations of `requests`, and we try all of them. When all requests in `requests` have been processed, we check `deltas` which is $n$ long and thus takes $O(n)$ time. When all requests have been processed that means we are at the bottom of the recursion tree, which in turn also means that any recursive state where every request has been processed is a leaf in the recursion tree. Because each level 'widens' by a factor of 2, this means that there are $O(2^{m-1})$ leaf nodes and we perform a $O(n)$ operation for each of them. The space complexity is $O(m+n)$ since the recursion stack has a size of $O(m)$, and `deltas` has a size of $O(n)$.  
  

