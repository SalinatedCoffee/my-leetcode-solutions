## 2196. (M) Create Binary Tree From Descriptions

### `solution.py`
Given the list of lists of length 3 `descriptions`, we are asked to return the root of the binary tree constructed using the information provided by `descriptions`. For each element of `descriptions`, the first item corresponds to the value of the parent node, the second to the value of the child node, and the third represents whether the child node is the left child of its parent(which is when its value is `1`). The value of each node is unique, and `descriptions` describes a valid tree. Because all nodes are unique, we can use a dictionary to quickly access a node by its value. We can also use a Python `set` to keep track of the nodes that have a parent so that we can identify the root node(the node that does not have a parent) without traversing the constructed tree. While iterating over `descriptions` we first check whether the parent and child nodes already exist as `TreeNode`s, instantiating new ones if not. The two nodes are then linked according to the value of the third item of the current element, after which the child node is added to the set `has_parent` to mark it as such. Once all elements of `descriptions` have been examined, we check each node against `has_parent` and return the one that does not have a parent.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `descriptions`. `descriptions` is iterated over exactly once, and since each element takes $O(1)$ time to process, the overall time complexity of this step is $O(n)$. Searching for the root also takes $O(n)$ time as the size of the dictionary `nodes` is bound by $n$. The space complexity is also $O(n)$ due to `nodes` and `has_parent`.  
  

