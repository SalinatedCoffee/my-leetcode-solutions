## 1232. (E) Check If It Is a Straight Line

### `solution.py`
The collinearity of two 2D vectors can be checked by using the equation $a_x b_y = a_y b_x$, which is derived from the formula of the cross product of two 3D vectors. Since we are given a list of coordinates instead of vectors, we need to translate the origin of all points to any one of the given coordinates.  

#### Conclusion
The time and space complexity of this solution is $O(n)$, where $n$ is the length of `coordinates`. Translating `coordinates` takes $O(n)$ time and space, and the colinearity check also takes linear time.  
This problem can also be solved without translating `coordinates` - for example, one could simply iterate across `coordinates` while checking the colinearity of **three** points.  

