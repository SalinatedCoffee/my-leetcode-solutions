## 106. (M) Construct Binary Tree from Inorder and Postorder Traversal

### `solution.py`
A different flavor of [problem #105](../../0105.%20(M)%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/Python3), the difference here is that we need to change the recursive relation to work with a postorder traversal instead of preorder.  
For a preorder traversal, an array can be split into three parts: `[[..L][..R]N]`, where the left and right subtree interval may be empty. We do not know where the root node is in the inorder list, so we take the last node in the preorder list and use it as the root. We then retrieve the root node's position in `inorder`, as the subarrays on either side of it will correspond to its left and right subtrees. If we remove the last item in `preorder` before recursing on it, we can recurse on the right subtree first without modifying `preorder` any further as the right recursive calls will 'consume' the nodes in the right subtree interval before entering the left recursive call.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes. The space complexity is also $O(n)$.  
  

