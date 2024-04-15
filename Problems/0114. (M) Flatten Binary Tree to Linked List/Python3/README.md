## 114. (M) Flatten Binary Tree to Linked List

### `solution.py`
We can easily solve this problem by maintaining an explicit ordered list of all visited nodes. This approach allows us to modify the tree after it has been traversed, eliminating the need to carefully keep track of which edge has been changed and which have not. In this solution, we traverse the tree with the iterative flavor of DFS, appending each node to the end of the list `preorder`. Once the traversal completes `preorder` will contain all nodes in the tree in NLR order, which we can simply iterate over to convert the tree into a 'linked list' as requested by the problem.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the tree rooted at `root`. Running DFS on a tree with $n$ takes $O(n)$ time, and appending a node to the end of `preorder` takes amortized $O(1)$ time. Hence, the overall time complexity will be $O(n)$. The space complexity is also $O(n)$, due to the stack `nodes` and the list `preorder`.  
  


### `solution_2.py`
The follow up  

#### Conclusion
  