## 909. (M) Snakes and Ladders

### `solution.py`
The first thing that instinctively comes to mind (at least for me) is to solve this with backtracking. However we quickly realize that at a certain square it isn't clear when or when not to backtrack. Considering other approaches, we can see that BFS can be effective since we are asked to return the *least* number of moves that can be made to reach the last square.  
This is one of those problems where coming up with a conceptual solution is easy but where the execution of implementing it into code is difficult. We first have to deal with the cell labels, which is done by counting the number of rows bottom-first and deciding whether to reverse the column number based on which row an element is in. We may now 'flatten' `board` into a 1D list for easy access to the elements of `board` via labels instead of indicies. Implementing the BFS traversal is rather trivial, where at a certain square we enqueue the 'descendant' squares (reachable squares from current with 1 more move) along with the number of moves taken to reach that square and repeat until the queue is empty. We may return early whenever we reach the last square since BFS guarantees that the shortest path to the destination is returned.  
One more thing to note is that cycles may be present depending on how the snakes and ladders are positioned, and so we also keep a `set` to keep track of visited nodes.

#### Conclusion
This solution runs in $O(n^2)$ time since there are $n^2$ squares total, and we do a fixed number (6 maximum) of operations on each of them. It also uses $O(6^{n^2})$ space since 6 elements are added to `seen` for each square. Further optimizations may be made by checking whether a square has been visited *before* queuing it in `seen`, or by using a list of length $n^2$ instead to keep track of visited nodes.  
  

