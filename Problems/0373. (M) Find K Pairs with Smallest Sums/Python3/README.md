## 373. (M) Find K Pairs with Smallest Sums

### `TMLE.py`
The obvious brute force approach for this problem is to simply compute the sums of all pairs and sorting them in ascending order after. This can be achieved in many ways, but we have opted to use a min heap here.  

#### Conclusion
The time and space complexity is $O(mn)$, where $m$ and $n$ are the length of `nums1` and `nums2` repectively.  
  

### `solution.py`
The first approach is too slow and there are improvements that can be made. Since both input arrays are already sorted in ascending order, we can use that fact to select upcoming pairs in the desired order. Obviously, the pair with the smallest sum would be the first value of both arrays (simply represented as `(0,0)`). The next pair then would either be `(1,0)` or `(0,1)`, whichever is smaller. If we assume the former was selected, we again have two choices. We can either choose `(1+1,0) = (2,0)` or `(1,0+1) = (1,1)`, whichever is smaller. However, we also have to consider `(0,1)` from the previous step. This can be performed in optimal time if we keep a min heap of all unchosen pairs. We also need to remember to keep track of pairs that have been selected since pairs need to be unique.  

#### Conclusion
This solution has a time complexity of $O(\text{min}(k\log k, mn\log(mn))$, where $k$ is `k`. The `while` loop iterates $O(\text{min}(k,mn))$ times. For each iteration we insert at most 2 elements into the min heap `pairs`, which takes $O(\text{min}(k\log k, mn\log(mn))$ time. The space complexity is $O(\text{min}(k,mn))$.  
  

