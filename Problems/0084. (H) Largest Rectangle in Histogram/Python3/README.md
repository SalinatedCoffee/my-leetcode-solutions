## 84. (H) Largest Rectangle in Histogram

### `TLE.py`
The brute force approach involves looking back in `heights` for all elements in `heights` while computing the area between the current bar and the one to its left. This algorithm quite obviously has a quadratic time complexity, and will fail with TLE.  

#### Conclusion
The time complexity of this algorithm is $O(n^2)$ where $n$ is the length of `heights`. The space complexity is $O(1)$.  
  


### `solution.py`
We ideally want a solution that runs in linear time. Going back to the problem description, we want the largest area in `heights`. Because we want the area of rectangles that are contained *within* the histogram, the height of a rectangle between two bars cannot be larger than the minimum height between those two bars. For example, if `heights = [0, 4, 1, 3]`, the height of the rectangle between `4` and `3` is `1`, resulting in an area of `3`. If we think about this in reverse, focusing instead on the single value `1`, we can see that `4` and `3` are essentially the last values larger than `1` to its left and right. Thus, we can reason that we could optimally compute the area of the largest rectangles where its height is bound by each value in `height`. In order to do this without resorting to algorithms with quadratic time complexity, we need to devise a method to retrieve the indices of the last largest value than `heights[i]` to the left and right of `i` in constant time. It turns out that we can do exactly that by using a (relatively) niche data structure known as a monotonic stack. As the name suggests, monotonic stacks use stacks to store elements, but the main feature of monotonic stacks is that its elements either strictly increase or decrease. This ordering is enforced by how items are pushed and popped to and from the stack. For this problem, we would need to implement an increasing monotonic stack as we want to find the first item that is smaller than some `heights[i]` to its left and right (which is identical to finding the last items larger than or equal to `heights[i]`). Simply put, we initialize a list and a stack and iterate over `heights`. The top of the stack is first examined, comparing it with the current element. If the current element is smaller, the top of the stack if popped off. This is repeated until either the stack becomes empty or the top element is larger than or equal to the current element. If the stack is not empty, the top of the stack is the first element smaller than the current element towards its left, and so we update the list accordingly. This algorithm can also be used for the other direction with small modifications.  
Once we have the two lists of indices, we can trivially compute the rectanglular area for every element in `heights` as mentioned previously, among which we return the largest.  

#### Conclusion
The time and space complexity for this problem is $O(n)$ where $n$ is the length of `heights`. Populating the two lists of indices, as well as computing the rectangular areas each take $O(n)$ time to complete. Also, the two lists of indices are kept in memory, and will use $O(n)$ space.  
  

