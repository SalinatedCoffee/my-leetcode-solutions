## 959. (M) Regions Cut By Slashes

### `solution.py`
A grid is represented by the list of strings `grid`, where the square on the `i`-th row and `j`-th column is represented by the `j`-th character in the `i`-th string of `grid`. Each square can be divided by a slash(`/`), a backslash(`\`), or not divided at all(` `). Given `grid`, we are asked to return the total number of regions divided by the slashes. For example, if `grid = [" /", "/ "]` we should be returning `2`.  
The first thing that comes to mind upon reading the problem description is connected components. If we can somehow represent the grid as a graph, appropriately disconnecting(or not connecting) nodes while iterating over `grid`, the number of connected components after every square in `grid` has been examined should be equal to the number of divided regions. We also recognize the need to use a union-find to model this problem since we are dealing with connected components of a graph. Now that we have an approach, we need to devise a method of translating the problem into a graph. Representing a square with a single node will not work since we cannot model the square being divided. If we think about how a square can be divided, we can see that its neighboring squares are connected through the square depending on how it is divided. If the square contains a `/` for example, the squares above and to the left of the square are connected as well as those below and to the right. Because of this, we should model a square as 4 separate nodes representing the cardinal directions. The connections between a square and its neighbors *always* occur regardless of how the square is divided. However, the connections between the 4 nodes of the same square differ depending on how it is divided. For instance, if a square contains a `/`, the nodes corresponding to the directions up and left will be connected, as well as those for down and right.  
Now that we have modeled the problem as a graph, we can start implementing a solution. The 3D list `p` will represent the parent node of the component that a node is a part of, and will be initialized with each node having itself as its parent. Functions `ufind` and `uunion` will be used to interact with the union-find, with the former returning the parent of a node and latter merging two nodes. Iterating over `grid`, we first make the 4 connections between a square and its neighbors. We then look at the current character and appropriately interconnect the 4 nodes of the square. Once the entirety of `grid` has been examined, the number of connected components in the union-find data structure will be the number of separate regions of the grid.  

#### Conclusion
This solution has a time complexity of $O(n^2)$ where $n$ is the height(or width) of `grid`. While `p` is a 3D list, only the first and second dimensions are bound by $n$ with the third being bound by the constant value 4. Thus, the initialization of `p` will take $O(n^2)$ time to complete. The node-connecting step will also require $O(n^2)$ time to run since the union-find is interacted with a fixed number of times for each square. An interaction on a graph with $n^2$ nodes takes $O(\alpha(n^2))$ time, with $\alpha(n^2)$ being the inverse Ackermann function. As this function is typically considered to be a constant, the overall time complexity comes out to be $O(n^2\cdot\alpha(n^2)) = O(n^2)$. The space complexity is also $O(n^2)$, due to `p`.  
  
