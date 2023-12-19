## 661. (E) Image Smoother

### `solution.py`
By far the simplest solution is the brute force approach where we explicitly compute the average for each and every cell. Because we cannot perform this in-place, we need to initialize a separate 2D list `ret` to store the smoothed values.  
We define a function `filter` which takes 2 arguments `y` and `x`. `filter` will return the smoothed value for the value in the `y`th row and `x`th column in `img` (0-indexed). The range of the 3x3 filter is computed after which the sum of the elements within that range is taken. Finally, we perform integer division on that sum with the number of cells within the filter range.  

#### Conclusion
This solution has a time complexity of $O(mn)$ where $m$ and $n$ are the dimensions of `img`. Initializing `ret` and calling `filter` for every value in `img` both take $O(mn)$ time. The space complexity is $O(1)$ excluding the return list `ret`.  
As is usually the case with simple problems such as this, there are many advanced approaches that can be taken to optimize the time / space complexities further. LeetCode's official [editorial](https://leetcode.com/problems/image-smoother/editorial) for this problem is very well written, and covers multiple approaches.  
  

