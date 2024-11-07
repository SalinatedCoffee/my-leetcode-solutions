## 2275. (M) Largest Combination With Bitwise AND Greater Than Zero

### `solution.py`
Given the list of integers `candidates`, we are asked to return the length of the longest subsequence of elements where the bitwise AND of all values is larger than `0`. Checking the problem constraints we can immediately see that a brute force approach will take too long as there will be a total of $2^n$ subsequences if `candidates` has a length of $n$. Returning to the problem description, we know that the bitwise AND 'sum' of a combination(subsequence) needs to be larger than `0` for it to be valid. This means that the binary representation of each of the elements in a valid combination has a raised bit in the same digit. Thus, if we know the number of elements with raised bits in each binary digit, we can easily determine the size of the largest combination which has a bitwise AND sum larger than `0`.  
We first initialize a `defaultdict` `counts` that has integers as values. The value of `counts[i]` will be the number of elements in `candidates` that has a raised bit in the `i`th binary digit. Iterating over `candidates`, we increment the appropriate values of `counts` for the current element. Once every element has been examined, we return the largest *value* in `counts`.  

#### Conclusion
This solution has a time complexity of $O(n\log m)$, where $n$ is the length of `candidates` and $m$ is the average binary length of the elements of `candidates`. Finding the raised bits of a single number $m$ takes $O(\log m)$ time, and this operation is performed on each and every element of `candidates`, putting the overall time complexity at $O(n\log m)$. The space complexity is $O(\log m)$, as a key-value pair in `counts` corresponds to a single binary digit of the elements of `candidates`.  
  

