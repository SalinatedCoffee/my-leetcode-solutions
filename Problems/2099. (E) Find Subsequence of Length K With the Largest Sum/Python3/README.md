## 2099. (E) Find Subsequence of Length K With the Largest Sum

### `solution.py`
Given the list of integers `nums` and integer `k`, we are asked to return the subsequence of `nums` with length `k` that has the largest sum. We can trivially solve this problem by realizing that the `k` largest elements of `nums` form the desired subsequence.  
We first augment the elements of `nums` with their indices, as this information is needed in order to return the *subsequence itself* rather than a simple list of elements. `nums` is then sorted in descending order of its elements, after which the first `k` items are copied into a separate list. This new list is sorted also, in ascending order of indices. Finally, we return the resulting list after stripping the index information from it.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$, where $n$ is the length of `nums`. The initial augmentation of `nums` takes $O(n)$ time to complete, with the following sorting step requiring $O(n\log n)$ time to finish. Slicing the sorted list, as well as stripping it of indices are $O(k)$ time operations. Sorting the sliced list has a running time of $O(k\log k)$. Summarizing, the overall time complexity is $O(n\log n + k\log k + n + k)$, but since $k$ is bound by $n$, the time complexity can also be written as $O(n\log n + n\log n + n + n)$, which simplifies to $O(n\log n)$. The space complexity is $O(n)$, due to the augmentation and sorting steps.  
  

