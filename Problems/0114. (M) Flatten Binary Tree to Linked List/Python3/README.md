## 114. (M) Flatten Binary Tree to Linked List

### `solution.py`
We can easily solve this problem by maintaining an explicit ordered list of all visited nodes. This approach allows us to modify the tree after it has been traversed, eliminating the need to carefully keep track of which edge has been changed and which have not. In this solution, we traverse the tree with the iterative flavor of DFS, appending each node to the end of the list `preorder`. Once the traversal completes `preorder` will contain all nodes in the tree in NLR order, which we can simply iterate over to convert the tree into a 'linked list' as requested by the problem.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the tree rooted at `root`. Running DFS on a tree with $n$ takes $O(n)$ time, and appending a node to the end of `preorder` takes amortized $O(1)$ time. Hence, the overall time complexity will be $O(n)$. The space complexity is also $O(n)$, due to the stack `nodes` and the list `preorder`.  
  


### `solution_2.py`
The follow up question asks us to implement a solution that does not use any extra memory. When asked to implement a constant-space algorithm when traversing trees, the usual approach involves implementing a flavor of something called the [Morris traversal](https://en.wikipedia.org/wiki/Tree_traversal#Morris_in-order_traversal_using_threading). This tree traversal algorithm modifies the tree being traversed into a [threaded tree](https://en.wikipedia.org/wiki/Threaded_binary_tree), which links nodes in a specific fashion by utilizing the unused pointers of a node(those that point to nothing). By slightly modifying Morris traversal, we can implement an algorithm that 'flattens' the tree while using only constant space.  
Say we are currently flattening a tree, and are currently on node `node`. There are 4 possible configurations when it comes to the children of `node`. `node` either has both left and right children, has only the left or right child, or has no children. Considering the trivial cases, we get:  

* If `node` only has a left child, we simply need to change it to be the right child.  
* If `node` has no children, then there is nothing else to do.  
* If `node` only has a right child, then `node` and its child node are already correctly linked.  

The case where `node` has both children is a bit more involved. Because we want to flatten the tree into a 'linked list' with the preorder ordering of the nodes, we know that the flattened list of the left subtree of `node` should come *before* that of the right subtree. Hence, it would be reasonable to argue that we should 'squeeze' in the left subtree between `node` and its right child to visit the nodes in the correct order. Linking the root of `node`'s left subtree is trivial, as we only need to make the left child the right child instead. But where should we link the original right child of `node`? The answer is the right child of the rightmost leaf node of the original left subtree of `node`(which is admittedly quite a mouthful).  Because we are traversing the tree from the left towards the right, the last node we will ever visit in a given tree will be the rightmost leaf. Thus, by attaching a node to the right side of that leaf node, we are essentially 'extending' the tree. Now that we know what we should be doing for each of all four cases, we can go ahead and implement the solution.  

#### Conclusion
The solution has a time complexity of $O(n)$ and a space complexity of $O(1)$, as requested by the follow up question.  

