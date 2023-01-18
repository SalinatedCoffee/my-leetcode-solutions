## 926. (M) Flip String to Monotone Increasing

### `solution.py`
The intuition is that we can compute an optimal value at a certain point by using values computed in the previous step. We can see that our intuition is indeed correct by reasoning that if a string is monotonically increasing, its prefixes are also monotonically increasing (by induction). So if at an index `i` we know the minimum number of flips we need to perform to make the substring ending with `i-1` valid, we can compute the number of flips required to make the substring ending at `i` valid based on those values. If `i` is `0`, we can do two things; we can either leave it as it is and make the preceding substring all `0`s by flipping all `1`s within it, or we can flip it to `1` and move on - whichever takes the smallest number of flips. If `i` is `1`, we may move on after incrementing a counter(for use in the previously mentioned case) since appending a `1` to a increasing substring always results in a valid string.  
So the solution first does a quick sanity check to handle strings of length 1, and then initializes a list and counter. Then it iterates through the provided string performing the aformentioned operations as necessary. The value for the entire string will be stored in the last element of `dp`.  
  
#### Conclusion
The time and space complexity is $O(n)$ where $n$ is the length of the given bit string. We traverse through the entirety of the string and we keep a list of length $n$ in memory to store the previously computed values.  
  
  
### `solution_2.py`
The first solution was fast, but we can improve it even further by noticing that to compute the value at some index `i` the only bit of information we need is the computed value at `i-1`. Thus instead of using a list of length `len(s)` to store the computed values at every position we can just store a single value that represents the minimum flips at the previous location.  
  
#### Conclusion
This solution runs in $O(n)$ time but uses $O(1)$ space.  
  

