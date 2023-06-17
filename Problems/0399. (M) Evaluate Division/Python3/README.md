## 399. (M) Evaluate Division

### `solution.py`
If you've ever taken a linear algebra class, you may be tempted to try and use matrices to solve this problem. However matrix operations are (mostly) not supported by default, and are non-trivial to implement from scratch. Instead, we can turn this into a graph problem given the problem constraints. The two main things to notice are that there will never be a contradiction (if an answer exists, it is the *only* answer) and variables such as `ac` is a unique variable instead of being a product of two variables `a` and `c`. Since the equations themselves are very simple, we can see that we can cancel variables out by multiplying two equations. For example, in `equations = [['a', 'b'], ['b', 'c']], values = [1.0, 2.0]`, we can multiply the two equations $a/b = 1.0$ and $b/c = 2.0$ to cancel out the variable $b$. We are then left with the equation $a/c = 1.0 \times 2.0$, which would be the answer to the query `['a', 'c']`. Thinking of this as a graph, we can see that we start at the numerator of the query, and follow a path to the denominator. The value of the RHS then, will be the product of all equations that have been 'traversed'.  
Thus we can construct a directed graph where an edge from `u` to `v` is weighted with the value of the fraction $u/v$. We need to also account for reciprocals, which we can represent with a reverse edge. Once the graph has been generated, we may simply try traversing the graph according to `queries`. If either variable does not exist in the graph or a path does not exist between then, it means that the answer cannot be determined. Else, the answer is the product of the weights of all edges in the path from the source node to the destination node.  

#### Conclusion
This solution has a time complexity of $O(mn+m^2)$, where $m$ is the length of `queries` and $n$ is the length of `equations`. BFS takes $O(|V|+|E|)$ time to run, and here $|V|$ is $n$ and $|E|$ is $m$. This is performed for every element in `queries`, hence $O((n+m)m) = O(mn+m^2)$. The space complexity is $O(n)$, since the graph can contain $O(n)$ nodes and edges. BFS will use $O(n)$ memory.  
  
