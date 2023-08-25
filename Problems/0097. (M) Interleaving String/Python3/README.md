## 97. (M) Interleaving String

### `TLE.py`
For `s3` to be '*interleavable*' by `s1` and `s2`, there are a few things to consider. We want to 'consume' all characters in `s1` and `s2` by the time we have verified `s3` is interleavable, and we must do so in order of which the characters appear in `s1` and `s2`.  
If we assume `s3` is in fact interleavable, and we split `s3` into half, it **must** be the case that these two halves are both interleavable. That is, the interleavability of `s3` relies on the interleavability of two of its substrings. This tells us that we should be taking a dynamic programming approach to this problem, which we will do so by first implementing a top-down solution.  
Say we are examining `s3[0]` and we have the entierety of `s1` and `s2` available to us. There are 2 choices that can be made in this state; if `s1[0] == s3[0]`, we can consume `s1[0]` and recursively examine the interleavability of `s3[1:]` using `s1[1:]` and `s2[:]`. Or, if `s2[0] == s3[0]`, we can recurse on `s3[1:]` using `s1[:]` and `s2[1:]`. Note that it may be the case that `s1[0] == s2[0] == s3[0]`, in which case we should try exploring both choices. Putting it more formally, function $f(i,j,k)$ returns whether `s3[k:]` is interleavable using `s1[i:]` and `s2[j:]`. That is,  
```math
f(i,j,k) =
\begin{cases}
f(i+1,j,k+1) & \text{if }\texttt{s1[}i\texttt{] == s3[}k\texttt{]} \\
f(i,j+1,k+1) & \text{if }\texttt{s2[}j\texttt{] == s3[}k\texttt{]} \\
f(i+1,j,k+1) \lor f(i,j+1,k+1) & \text{if }\texttt{s1[}i\texttt{] == s3[}k\texttt{]}\land\texttt{s2[}j\texttt{] == s3[}k\texttt{]}
\end{cases}
```
The states in our recurrance relation has 3 integers as parameters, and is trivial to memoize. By definition we want the value of $f(0,0,0)$, which we can return immediately.  

#### Conclusion
The algorithm described above has a time complexity of $O(mnk)$, where $m$, $n$, and $k$ are the lengths of `s1`, `s2`, and `s3`, respectively. `i` is in the range `[0, len(s1))` and `j` is in the range`[0, len(s2))`, and as such there are $O(mn)$ possible states which need to be computed. `dp` is a $m\times n\times k$ 3D list, and takes $O(mnk)$ time to be initialized. The space complexity is also $O(mnk)$.  
  

### `solution.py`
The first solution, while correct, takes too long to run and fails with TLE upon submission. Going back to the TC analysis we notice that the actual computation step only takes $O(mn)$ time, and intializing `dp` outscales this operation by a factor of $k$. At this point we realize that we only need *2* parameters to represent a single state, since `k` depends on `i` and `j` and thus can be trivially computed through the expression `i+j`. After reducing `dp` down to a 2D list and making adjustments to the recurrence relations accordingly, we arrive at a solution that passes without TLE.  

#### Conclusion
The time and space complexity of this solution is $O(mn)$.  
  

