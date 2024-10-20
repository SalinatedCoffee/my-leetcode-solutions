## 1545. (M) Find Kth Bit in Nth Binary String

### `solution.py`
The bitstring $s_i$ is constructed by concatenating $s_{i-1}$ with a single `1`, and then the reverse of the inverse of $s_{i-1}$. If $s_0$ is `0`, we are asked to return the `k`th bit(1-indexed) of the string $s_{\texttt{n}}$. Because `n` is rather small, we can take a brute force approach that actually generates each string from $s_0$ up to $s_{\texttt{n}}$.  

#### Conclusion
This solution has a time complexity of $O(2^n)$, where $n$ is `n`. The space complexity is also $O(2^n)$.  
  


### `solution_2.py`
Instead of brute forcing the solution, we can take a more sensible approach by simulating the generation of each bitstring. Because each string is essentially the string from the previous step mirrored at the center, we can determine which bit we want from the previous step. For example, if the `n`th string has a length of `l`, `k` is the `k`th bit from the first half if `k < l // 2`, `1` if `k == l // 2`, or the `l - k`th bit of the second half if `k > l // 2`.  

#### Conclusion
This solution has a time complexity of $O(n)$. The space complexity is also $O(n)$, since the recursion stack will have a maximum height of $n$.  
  

