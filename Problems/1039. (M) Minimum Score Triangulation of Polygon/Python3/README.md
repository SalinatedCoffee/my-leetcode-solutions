## 1039. (M) Minimum Score Triangulation of Polygon

### `solution.py`
`values` is a list of vertex weights of a convex polygon, in clockwise order starting with `values[0]`. A weight of a triangle is simply the product of the weights of the vertices comprising that triangle. Given `values`, then, we are asked to return the minimum weight sum when triangulating the original polygon formed by the vertices in `values`. Triangulating a polygon involves dividing it into multiple non-overlapping triangles; a triangulation of a polygon with `n` vertices should result in `n-2` triangles.  
Thinking about the problem, we can vaguely see that we might be able to solve it through a recursive approach. This is because that forming a triangle inside the original polygon splits the polygon into multiple sub-polygons. Since these sub-polygons inherit the characteristics of its parent, we can apply the same set of logic to these pieces, and vice-versa. Now that we have decided upon an approach, we need to define the state and recurrence relation between the states.  

#### Conclusion
\<Content\>  
  

