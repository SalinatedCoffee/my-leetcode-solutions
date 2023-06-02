## 2101. (M) Detonate the Maximum Bombs

### `solution.py`
At first glance this may look like a union-find problem since we need to 'cluster' bombs that can be detonated by each other. However union-find is analogous to undirected graphs, but here the relationship between bombs are directed(bomb A detonating bomb B does not guarantee the opposite). Instead we may explicitly generate a directed graph, and run some graph traversal algorithm from every node while counting the number of nodes that have been traversed. For this solution, we have used the iterative version of DFS. As an optimization, we should check/mark a node as visited right before we push a node onto the stack to avoid re-traversing a node multiple times.  

#### Conclusion
The time complexity of this problem is $O(n^3)$ where $n$ is the number of bombs. Populating `adj` takes $O(n^2)$ time, and DFS is performed for every bomb. DFS takes $O(|V|+|E|)$, but here $|E| = n$ and $|V| = O(n^2)$ (there can be at most $n^2$ edges). The space complexity is $O(n^2)$.  
  

