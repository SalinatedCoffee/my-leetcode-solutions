## 1187. (H) Make Array Strictly Increasing

### `solution.py`
The intuition here is taking a dynamic programming approach since we have a value that we want to optimize, and there are clear transitions between states. Say we iterate along `arr1` while making sure that at some index `i` the prefix `arr1[:i]` strictly increases. When we are at index `i` then, what choices can we take?  
If `arr1[i-1] >= arr[i]`, we **must** reassign `arr1[i]` in order to make `arr1[:i+1]` strictly increasing. The optimal value we can take from `arr2` is the smallest value larger than `arr1[i-1]`, since we would like to minimize the new value at index `i` to maximize the chances that subsequent values are larger than `arr1[i]`. To do this, we may pre-sort `arr2` and run binary search since we can arbitrarily select items from `arr2` for any value `arr1[i]` which allows us to simply ignore the position of the values themselves.  
If `arr1[i-1] < arr1[i]` there are two actions that we can take. We can either leave the value of `arr1[i]` as is and move on, or we can replace the value with the smallest value in `arr2` that is larger than `arr1[i]`. Either way we want to **minimize** the total number of operations, hence we choose the option that requires less operations that have to be performed.  
Now we can implement a recursive solution, where the function `recurse()` takes two arguments - the current `arr1` index `i`, and the value of `arr1[i-1]`. When `i = 0`, we arbitrarily set this value to `-1`. We can do this without affecting the result because the values of the elements in both arrays are at least `1`. The answer we want is the return value of `recurse(0, -1)`, which we can return directly if it is a valid value.  

#### Conclusion
The time complexity of this solution is $O(m(m+n)\log n)$ where $m$ and $n$ are the lengths of `arr1` and `arr2`, respectively. Sorting `arr2` takes $O(n\log n)$ time. For `recurse(i, prev)`, there are $m$ possible values for `i` and $O(m+n+1)$ possible values for `prev`, since we can assign any value from `arr2`. For each call to `recurse()` we perform a binary search on `arr2`, which takes $O(n)$ time. The space complexity is $O(m^2+mn)$.  
  

