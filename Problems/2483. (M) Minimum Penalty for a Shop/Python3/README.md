## 2483. (M) Minimum Penalty for a Shop

### `solution.py`
At some hour `i`, the total penalty of closing at that hour will be the sum of the number of `N`s in `customers[:i]` and the number of `Y`s in `customers[i:]`. Instead of counting from scratch for all possible `i`, we can precompute these counts by generating prefix and suffix sums for all indexes in `customers`. We iterate over `customers` two times, once from left to right, and once in the reverse direction. For the left-to-right run, we count and increment the number of `N`s in such a way that `prefix[i]` contains the number of `N`s in the prefix `customers[:i]`. The same can be said for the suffix sums, except we count the number of `Y`s and `suffix[i]` should be **inclusive** (accounts for `customers[i:]`) as closing at hour `i` means that the store should be considered closed at that hour.  
Once the prefix and suffix sums have been computed, we simply search for the earliest hour that incurs the smallest penalty and return that hour.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `customers`. We iterate over `customers` exactly three times, and during each iteration we perform a fixed number of constant-time operations. The space complexity is also $O(n)$, since we use a list of length $n+1$ to store the total penalty for all possible closing hours.  
  

### `solution_2.py`
In the previous solution we had to traverse `customers` thrice in order to compute the pre/suffix sums and find the desired closing hour. This can be compressed into a single pass by noticing that the magnitude of the penalties do not matter, since we only want the closing hour with the smallest penalty. Instead, we can compute the relative penalty of all closing hours to determine the hour with the least penalty. Consider two closing hours `i` and `j`, where `i < j`. If `customers[i:j]` contains `k` `Y`s, that would mean that `i` would have `k` *more* penalty than `j`. The same can be said for `N`s, except that `i` woule have `k` *less* penalty than `j`. As such, we can simply iterate over `customers` while keeping track of the current relative penalty. If a `Y` is encountered at hour `i`, it means that closing at the next hour would *decrease* the penalty by `1`, and thus we would need to **decrement** the running penalty by `1`. Otherwise, we **increment** the penalty by `1`. Once the running penalty is updated, we check if it is less than the previously seen smallest penalty and update the minimum penalty and closing hour accordingly. As mentioned previously the relative penalty at index `i` represents the penalty of closing hour `i+1`, and so we must update the closing hour accordingly.  

#### Conclusion
The time complexity is $O(n)$. The space complexity is $O(1)$ since we use a single integer to store the relative penalty instead of a list of length $n+1$ in the first solution.  
  

