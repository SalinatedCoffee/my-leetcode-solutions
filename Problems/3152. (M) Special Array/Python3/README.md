## 3152. (M) Special Array

### `solution.py`
An array of integers is special if the oddity of all adjacent pairs are different. For example, the array `[1, 2, 3, 4, 5]` is special, but `[1, 1, 2, 2, 3]` is not. A single query involves 2 integers representing the start and end of a subarray of the given array `nums`. Our task is to evaluate all queries in the list `queries` and return the list of results.  
Obviously, a subarray must not contain a pair with same oddity for it to be special. Because we are considering only adjacent pairs, we can image a special array as a continuous chain of integer pairs that have different oddities. If an array contains a 'discontinuous' pair, we can say that the array cannot possibly be special. Is there a way that we could efficiently determine whether a subarray is continuous given the indices of the first and last elements in said subarray? Say that we know the index of the first element in the longest special subarray that ends with some element `i`, for all possible `i`. For the subarray `nums[l:h+1]` to be special, this index **must** be identical for the `l`-th element and the `h`-th element. The problem can now be solved by precomputing the index for each element of `nums`, and then iterating over `queries` while evaluating the result of each query.  

#### Conclusion
The time complexity of this solution is $O(m+n)$, where $m$ is the length of `queries` and $n$ is the length of `nums`. `nums` is iterated over to compute the starting position of the longest special subarray that ends with each element, and completes in $O(n)$ time. We then iterate over `queries` to process each query using the precomputed values, using $O(1)$ time to evaluate a single query. Since there are $m$ queries total, the overall time complexity of this solution comes out to be $O(m+n)$. The space complexity(excluding the returned list `res`) is $O(n)$, due to the list of indices `start`.  
  

