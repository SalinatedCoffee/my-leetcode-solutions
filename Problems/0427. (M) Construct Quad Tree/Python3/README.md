## 427. (M) Construct Quad Tree

### `solution.py`
Recursion is a tree problem's best friend, and we can immediately see that we can apply recursion to solve this problem. The recursive function simply takes a coordinate (pointing to the upper-left square) and the size of the square, and then checks whether the square is uniform by computing the sum of its elements. If it is, it simply returns the corresponding `Node` object marked as a leaf. If it isn't, it recurses on its 4 sub-squares and returns a `Node` object with those 4 sub-squares as its children.  
Thankfully, the constraints on the size of the grid saves us from the hassle of dealing with edge cases on the size and dimensions of the squares.  
  
#### Conclusion
The time complexity is $O(n^2 \log n)$ where $n$ is the length of `grid`. For each recursion level we iterate through all values in `grid`, and the maximum recursion depth is $\log_4 n^2$ which simplifies to $\log n$. Consequently, the space complexity is $O(\log n)$ as the recursion stack is the only scaling component in total memory usage.  
  

