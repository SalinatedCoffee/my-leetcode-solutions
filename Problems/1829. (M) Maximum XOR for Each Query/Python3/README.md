## 1829. (M) Maximum XOR for Each Query

### `solution.py`
Given the sorted array of integers `nums` and integer `maximumBit`, we are asked to return an array containing the value of `len(nums)` number of queries. A single query involves the following rules:  

- The result of the query `k` must be strictly less than `2**maximumBit`.
- `k` should maximize the value of `nums[0]` XOR `nums[1]` XOR ... XOR `nums[-2]` XOR `nums[-1]` XOR `k`.  
- After the value of a query has been determined, the last element of `nums`(`nums[-1]`) should be removed from `nums`.  

There are a few things that we can observe from these rules. Firstly, because the *last* element of `nums` gets removed after a query, we know that the XOR sum of the prefix `nums[:i+1]` will be used in the `n - 1 - i`th query. Secondly, we want to find the value `k` that maximizes the XOR sum of it and the prefix of `nums` corresponding to the query. In order to maximize the resulting value of XORing a constant(XOR of the prefix of `nums`) and some number(`k`), we want to flip all `0`s in the constant to a `1`. This value can easily be determined by XORing the constant with a value that has all of its binary bits raised, as the existing `1`s in the constant will be flipped to `0` and the `0`s to `1`s.  
Combining these observations, we can start implementing the solution. We first initialize the bitmask that will be used to evaluate `k` for each query by evaluating the expression `2**maximumBit - 1`. After initializing the list of query results `res` and current XOR sum `cur`, we start iterating over `nums`. The XOR sum of the current prefix is computed first before determining the value of `k`, which is simply the value of `cur ^ mask` as described above. As the prefix `nums[:i+1]` corresponds to the `n - 1 - i`th query, we store the value of `k` in `res[n-1-i]`. Once the entirety of `nums` has been examined, we simply return the list `res` directly.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. All elements of `nums` are examined, and since each element takes $O(1)$ time to process the overall time complexity comes out to be $O(n)$. The space complexity is $O(1)$, excluding the return list `res`.  
  

