## 997. (E) Find the Town Judge

### `solution.py`
Flavor text aside `trust` looks awfully like a list of edges, and so we'll treat this problem like a graph problem. '`a` trusting `b`' can be nicely translated to 'there is a directed edge from `a` to `b`', and in this context we can see that a 'judge' node will have `n-1` incoming edges and 0 outgoing. Thus we can keep counters for all nodes and iterate through `trust`, incrementing a node's counter for every incoming edge and decrementing for an outgoing edge. Finally we can scan through the counters and return the index of the counter with the value `n-1`.  

#### Conclusion
This solution runs in $O(n^2)$ time since the maximum number of edges a directed graph can have is $n(n-1)$. The space complexity is $O(n)$ because we keep a single list of length $n$ in memory.  
  

