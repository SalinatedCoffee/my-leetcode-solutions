## 2530. (M) Maximal Score After Applying K Operations

### `solution.py`
`nums` is a list of integers, and we are allowed to perform `k` operations on its contents. During a single operation, we can arbitrarily select an element `nums[i]`, add its value to the total score, and replace it with the value of `ceil(nums[i] / 3)`. Given these conditions, we are asked to return the maximum achievable score.  
We can immediately see that an optimal selection of elements exists for this problem, and thus we can implement a greedy algorithm to solve this problem. Because we want to maximize our score we would want to select the element with the largest value in `nums` for each and every operation. If we simply sort `nums`, `nums` would not be sorted once we perform a single operation as the selected element would now be a third of its original value. We want to make sure that the element of `nums` are always in sorted order, which can be achieved with a heap.  
`nums` is converted into the max heap `items`, and the total score `res` is initialized as `0`. We then start performing the operations, removing the first item off the heap, adding its value to `res`, and pushing the appropriate value back onto the heap. After repeating these steps `k` times, `res` will contain the desired value.  

#### Conclusion
This solution has a time complexity of $O((n+k)\log n)$, where $n$ is the length of `nums` and $k$ is `k`. Converting `nums` into a heap requires $O(n\log n)$ time. Insertions and removals from this heap each take $O(\log n)$ time to complete. A single operation performs a single insertion and a single removal from `items`, bring its time complexity to $O(\log n)$. Since `k` operations are performed, the overall time complexity comes out to be $O(n\log n + k\log n) = O((n+k)\log n)$.  
  

