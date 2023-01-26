## 974. (M) Subarray Sums Divisible by K

### `TLE.py`
When we generate a prefix sum, we can see that we may compute the sum of `nums[i+1:j+1]` through `prefix[j] - prefix[i]`. From this we find that we can count the number of k-divisible subarrays by evaluating the previously mentioned expression for all pairs of `i` and `j` where `i < j`. While algorithmically correct, this method is not fast enough as it TLEs on inputs with sufficiently large `nums`.  

#### Conclusion
This algorithm takes $O(n^2)$ time to run using $O(n)$ space.  
  

### `solution.py`
By using the fact that we're dealing with modulo operations, plus a little bit of math we can come up with a better solution. We've already established that `prefix[j] - prefix[i] == sum(nums[i+1:j+1])` (sum of the subarray with interval $(i, j]$). Since we're looking for cases where the subarray sum is k-divisible, we can rewrite the expression in quotient-remainder form:
$$
(pj_q * k + pj_r) - (pi_q * k + pi_r) = sa_q * k + sa_r
$$
But here, we want the RHS to be divisible by $k$, so we can eliminate $sa_r$.
$$
(pj_q * k + pj_r) - (pi_q * k + pi_r) = sa_q * k
$$
Expanding terms, we get
$$
pj_q * k - pi_q * k + pj_r - pi_r = sa_q * k
$$
Here we can eliminate 3 terms by taking the modulo of the entire expression:
$$
((pj_q * k)\hspace{-0.4cm}\mod k) - ((pi_q * k)\hspace{-0.4cm}\mod k) + (pj_r\hspace{-0.4cm}\mod k) - (pi_r\hspace{-0.4cm}\mod k) = ((sa_q * k)\hspace{-0.4cm}\mod k)
$$
But since $x_r$ is the remainder after dividing by $k$, we know that $x_r \lt k$. Thus the previous expression simplifies to
$$
pj_r - pi_r = 0 \\
pj_r = pi_r
$$
Which tells us that if `prefix[j] % k == prefix[i] % k`, `sum(nums[i+1:j+1])` is also divisible by `k`.  
Using this, we can compute the number of k-divisible subarrays in the interval `[0, i]` by *counting* the number of subarrays that have the same remainder as `prefix[i] % k`. This eliminates the need to compare all possible pairs as was done in `TLE.py`, along with keeping the prefix sums of all elements in memory.  
The solution keeps track of the number of subarrays with remainder `r` in `modGroups[r]`. Iterating through `nums` the solution computes `prefix[i] % k = r`, and looks at `modGroups[r]` to get the number of `r`-remainder subarrays. Finally, it increments `modGroups[r]` by 1 to account for `prefix[i] % k == r`.  
  
#### Conclusion
The time complexity for this solution is $O(n)$. The space complexity is $O(k)$, where $k$ is the provided divisor `k`.  
  

