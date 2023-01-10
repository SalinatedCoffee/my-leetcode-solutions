## 173. (M) Binary Search Tree Iterator

### `solution.py`
One deceptively simple approach is to just do the traversal during the initialization step and keep the values in memory, as shown in this solution(implemented iteratively, since the recursive implementation is trivial). Subsequent calls to `BSTIterator.next()` and `BSTIterator.hasNext()` merely checks if there are any values remaining in `self._val`, which contains the values of all nodes in LNR order.  
  
#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the number of nodes in the tree. The space complexity is also $O(n)$ since we keep the values of all nodes in memory. Memory is also used by the internal stack in ``__init__`` - $O(h)$ where $h$ is the height of the tree. The overall space complexity is $O(n+h) = O(n)$(instead of $O(2n)$ since the height of the tree will never be *larger* than the number of nodes).  
Analyzing ``next()`` and ``hasNext()`` in isolation, they take $O(1)$ time and space since the traversal is already completed allowing us to find the next node in constant time. Overall, ``next()`` and ``hasNext()``  *technically* runs in average $O(1)$ time, but I would very hesitantly actually call it that since most(if not all) of the running time is front-loaded in the initialization step.  
  

### `solution_2.py`
The follow up problem asks whether if we could come up with a solution that runs in average $O(1)$ time using $O(h)$ memory - and we certainly can! As a matter of fact, we can deconstruct the first solution into two parts so that the traversal is 'paused' whenever we encouter a node without a left subtree. During object initialization we decend furthest down the left subtree until we hit a dead end, after which we stop traversing with `self._current = None` and the first inorder node on top of `self._stack`. When `next()` is called, we see that `self._current == None` is `True` and so we pop a node off `self._stack`, set the right subtree as `self._current`(so that the next call to `next()` traverses furthest down the left subtree), and then return `TreeNode.val` of the popped node(effectively 'pausing' the traversal).  
`hasNext()` is even simpler since the only case where a node does not have a next inorder node is when the tree is empty, which we can trivially check for by looking at `self._current`(`None` when the previously touched node has no left subtree) and `self._stack`(empty when there are no more nodes to backtrack to).  
  
#### Conclusion
Instantiation of `BSTIterator` will take $O(h)$ time using $O(h) memory. Subsequent calls to `next()` can take either $O(h-1)$ time (when the current node has a left subtree of height $h$) or $O(1)$ time(when current node does not have a left subtree). Overall however we touch(as in the entire process of push-pop-returning) all nodes in the tree exactly once, which means that on average `next()` runs in $O(1)$ time. On top of that since we don't keep the traversed nodes in memory, `BSTIterator`(`self._stack`, to be exact) uses $O(h)$ space. `hasNext()` has a time and space complexity of $O(1)$ since all it does is check the value of two variables.  

