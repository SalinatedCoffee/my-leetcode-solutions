## 209. (M) Minimum Size Subarray Sum

### `solution.py`

We are trying to minimize the length of a subarray which has at least `target` as its sum. Because of this, we can ignore any subarray that has a sum less than `target`. `nums` only includes positive integers and thus it stands to reason that removing or adding an element will **always** decrease or increase the subarray sum, respectively. A sliding window approach will work well here because we are dealing with sub*arrays*, and the addition and removal of an element from a subarray both exhibit well-defined behavior.  

Iterating over `nums`, we keep track of the first item in the currently considered subarray in `l`. For each element in `nums`, we add that value to the sum of the current subarray after which we check whether the sum is larger than `target`. If so, we try and make the subarray as shortest as possible by advancing `l` (and updating the sum accordingly) until the sum is less than `target`. By updating the shortest length seen (`ret`) during this step, we will have the desired value after the iteration has completed. If `ret` still holds its initial value it means that no such subarray exists, so we return `0`.  



#### Conclusion

This solution has a time complexity of $O(n)$ where $n$ is the length of `nums`. `nums` is iterated over once, and the nested `while` loop will at most loop `n` times since the comparison implicitly depends on the value of `l`. The space complexity is $O(1)$.  



#### Follow-up

The follow-up (oddly) asks us to implement a $O(n\log n)$ solution. This can be achieved by precomputing prefix sums of all elements and running binary search on them. If we know the prefix sums of indices `i` and `j` where $i < j$, the sum of the array between the two indices is simply `prefix[j] - prefix[i]`. Using this formula we can determine what the value of `j` would be if the sum of the subarray `nums[i:j]` is at least `target` by performing a binary search on `nums[i:]` looking for value `prefix[i] + target`.  

`nums` is iterated over once, and for each step we perform a binary search on a subarray of `nums`, which takes $O(\log n)$ time - hence the overall running time of $O(n\log n)$.  




