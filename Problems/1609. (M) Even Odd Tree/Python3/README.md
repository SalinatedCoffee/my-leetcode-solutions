## 1609. (M) Even Odd Tree

### `solution.py`
As the conditions change based on the height of a node, we want to traverse the given tree level by level. The easiest way of achieving this is by performing BFS, which will allow us to visit the nodes in order of their height and position within that height. Here, we have chosen to implement the iterative version of BFS which uses a queue to store nodes yet to be traversed. As we traverse the tree, we keep track of 2 variables; the height and value of the previous node. After retrieving a node from the queue, we first check the evenness of its value against its height. If correct, we add its children onto the queue before determining whether the node is the first within its 'row'. This can be done by comparing the node's height to that of the previous. If the node is indeed the first, we update the height and value of the previous node and move on to the next node. Otherwise, we check for monotonicity within the row by comparing the current node's value with the previous one. If at any point during the traversal it is determined that a node is 'invalid', we can immediately return `False`. If the traversal exits normally, we return `True` since all nodes are valid.  

#### Conclusion
This solution has a time and space complexity of $O(n)$ where $n$ is the number of nodes in the tree rooted at `root`. Every node in the tree is visited exactly once, and each node takes $O(1)$ time to process. The queue can hold $O(n)$ nodes, hence the space complexity of $O(n)$.  
  

