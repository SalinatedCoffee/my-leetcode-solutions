## 2444. (H) Count Subarrays With Fixed Bounds

### `solution.py`
First let's start off by figuring out how to compute the number of valid subarrays if the array only contains values that are inclusively within the provided range. Suppose we are given the array `[3, 2, 5, 1, 3, 6, 2]` and range `minK = 1`, `maxK = 6`. Valid subarrays *must contain both* `1` and `6`, as all other values are between the bounds. Thus the smallest valid subarray would be `[1, 3, 6]`. From here, we can try and 'expand' this subarray in each direction and count until we reach the ends of the array. From the smallest array we can expand the left side 3 times, resulting in a count of 4. We can also expand the right side by 1, and expand the left side 3 times again which would result in 4 more subarrays. From this we can see that we can compute the number of valid subarrays given 4 values; the position of the first number within bounds, the positions of the min/max values, and the position of the last number within bounds.  
This is where I got stuck for the longest time - my initial approach was to iterate through `nums` first, and *then* compute the number of subarrays by using the indices saved during the iteration. But what we can instead do is compute the number at each and every position. Then, we don't have to consider the case where we expand towards the right as that will be naturally taken care of while moving through `nums`. So we keep track of 3 values - the index of the most recent number out of bounds, and the indices of the most recent occurrence of `minK` and `maxK`. For some index `i` we can compute the number of valid subarrays expanding out towards the left as explained earlier. As `i` will also be our loop variable we also naturally count valid subarrays expanding towards the right.  
We can also save us the hassle of micromanaging conditionals by initializing the indices to `-1` and using `max()` to update `res`.  

#### Conclusion
This solution runs in $O(n)$ time where $n$ is the length of `nums`. The space complexity is $O(1)$.  
  

