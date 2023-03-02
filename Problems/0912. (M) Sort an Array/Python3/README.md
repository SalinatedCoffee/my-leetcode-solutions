## 912. (M) Sort an Array

### `solution_merge.py`
For this problem, we can implement any sorting algorithm we want as long as the time and/or space complexity is at least $O(n\log n)$. There are many algorithms that meet this condition but the official solution implements 4 of them; Merge Sort($O(n\log n)$, $O(n)$), Heap Sort($O(n\log n)$, $O(\log n)$), Counting Sort($O(n+k)$, $O(n)$), and Radix Sort($O(d(n+b))$, $O(n+b)$). Here we will be implementing the recursive flavor of [Merge Sort](https://en.wikipedia.org/wiki/Merge_sort).  
Merge sort is a divide-and-conquer algorithm that recursively splits the list in half, sorts the sublists, and merges them back together - hence the name. We can either sort in-place or allocate a new list and add the sorted items there, either way we need extra space equal to the size of `nums` which is why merge sort has a space complexity of $O(n)$.  
`sort(l, h)` recursively sorts `nums` from `l` to `h`, and `merge(l, m, h)` merges the two lists of ranges `[l, m]` and `[m, h]`.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `nums`. At every recursion depth all elements of `nums` is touched, and the height of the recursion tree is $\log n$ since each recursive call is called on a subarray half the size of the original. The space complexity is $O(n)$ as we sort in-place and use a temporary list `temp` with length `len(nums)`.  
  

