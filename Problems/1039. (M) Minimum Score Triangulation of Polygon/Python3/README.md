## 1039. (M) Minimum Score Triangulation of Polygon

### `solution.py`
`values` is a list of vertex weights of a convex polygon, in clockwise order starting with `values[0]`. A weight of a triangle is simply the product of the weights of the vertices comprising that triangle. Given `values`, then, we are asked to return the minimum weight sum when triangulating the original polygon formed by the vertices in `values`. Triangulating a polygon involves dividing it into multiple non-overlapping triangles; a triangulation of a polygon with `n` vertices should result in `n-2` triangles.  
Thinking about the problem, we can vaguely see that we might be able to solve it through a recursive approach. This is because that forming a triangle inside the original polygon splits the polygon into multiple sub-polygons. Since these sub-polygons inherit the characteristics of its parent, we can apply the same set of logic to these pieces, and vice-versa. Now that we have decided upon an approach, we need to define the state and recurrence relation between them. Dividing a polygon by creating a triangle is a good place to start. Unfortunately, this means that each state would have to be represented by 3 variables; and with each variable being bound by `len(values)`, the time complexity of this approach would be $O(n^3)$. Another problem with this approach(to a lesser extent) is that the number of resulting sub-polygons is varied. To remedy these issues, we can simply split the polygon in half by drawing a single edge. We can 'defer' the creation of triangles that include said edge to recursion, which will eventually reach base cases that include the edge. With this method, we can represent each state as a subarray of `values`. The value of `dp[i][j]` will represent the minimum weight sum of the triangulation of the polygon formed by the vertices in `values[i:j+1]`. If we were to select an arbitrary vertex `k` in `values[i+1:j]`   

#### Conclusion
\<Content\>  
  

