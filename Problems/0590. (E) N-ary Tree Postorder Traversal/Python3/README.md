## 590. (E) N-ary Tree Postorder Traversal

### `solution.py`
Given the root of an N-ary tree `root`, we are asked to return a postorder list of its node values. This can be trivially achieved through recursion by recursing down on a node's children in left-to-right order.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the number of nodes in the N-ary tree rooted at `root`. The space complexity is also $O(n)$, due to the call stack.  
  

### `solution_2.py`
The recursive version of the traversal was trivial, but the iterative version is a little bit involved. This is because postorder traversal requires us to visit each node twice; first when it is initially visited, and a second time to process its value after visiting all of its descendants. Because of how the recursive algorithm behaves, this behavior is implicitly taken care of which allows us to easily implement said algorithm. Using a stack, we need to explicitly implement this behavior to process each node value in the correct order. What if instead, we simply process a node's value as soon as it is visited so that we do not have to bother with revisiting the node again? This means that we will end up processing the node's values in NLR order, whereas the order we actually want is LRN. By now we can see that if we visit the child nodes in reverse order(NRL), and then reverse the list of node values(LRN), we will end up with the postorder list of node values. An iterative preorder traversal is trivial to implement, but we need to make sure that the children of a node is pushed onto the stack in the correct order. We want to visit the child nodes from right to left, which means that we should push them onto the stack starting with the leftmost child.  

#### Conclusion
The time and space complexity of this solution is identical to the previous solution, but will run faster in practice as the overhead from recursive function calls no longer exist.  
  

### `solution_3.py`
A solution that actually process the node values in postorder is also possible if we can handle the revisiting of nodes mentioned in the previous solution. We had already established that a node is visited once before processing its children and once after, with its value being processed during the second visit. This can be easily checked by using slightly more memory by marking a node's visited state when pushing it onto the stack. A single boolean can represent this state, with `False` indicating that a node has never been visited before and `True` meaning that it has already been visited. When a node is popped off of the stack and this flag is `False`, we push the node back onto the stack with the flag set to `True` before iterating over its children in reverse order. If the flag is `True`, its children have already been visited and processed, so we add the node's value to the list of values.  

#### Conclusion
The time and space complexity of this solution is identical to the previous solutions.  
  

