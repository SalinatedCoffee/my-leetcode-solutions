## 1970. (H) Last Day Where You Can Still Cross

### `solution.py`
Each day a land cell is replaced with a water cell. If we reverse this, this means that a land cell is **added** for every time step. Since we are incrementally adding components and checking whether these components are connected, we can take a union-find approach for this problem. Iterating along `cells` in reverse order, we connect the newly added land cell to any neighboring land cells. If the top and bottom are part of the same component, we can return the index of the current land cell. The trick here is figuring out how we can factor in the top and bottom in our implementation. For starters, there may be multiple landmasses bordering the top and bottom edges. Instead of running find between all of these landmasses, we can create two 'sentinel' nodes that the bordering cells can point to. We also want to use union by size instead union by rank as we have no need for arbitrary ranks and it is more efficient.  

#### Conclusion
The time complexity is $O(mn)$ where $m$ and $n$ are `row` and `col`, respectively. We iterate over `cells` in reverse (which is `row * col` long), and during each iteration we perform a fixed number of operations on the DSU. Find and union operations on a DSU are considered to run in constant time, hence the overall running time of $O(mn)$. The space complexity is also $O(mn)$ due to `turnstile` and the DSU.  
  

