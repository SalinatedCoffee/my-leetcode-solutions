## 606. (E) Construct String from Binary Tree

### `solution.py`
It is obvious that we should recursively traverse the tree, and the problem tells us outright to use a preorder traversal. The only catch is that we should be omitting empty parentheses that "do not affect the one-to-one mapping relationship between the string and the original binary tree". What this *actually* means that we should be able to reconstruct the original tree using the generated string - that is, if a node has a right child but no left one, the string should reflect that by using an empty parentheses pair to denote it.  
We define the recursive function `dfs(node)`, which will return the appropriate string representation of the subtree rooted at `node`. `l` and `r` are initialized with empty strings, after which they are assigned the parenthesized return values of calling `dfs()` on `node`'s left and right nodes respectively(if they exist). Finally, we check for the special case where `node` has a right child but no left child. If so we return a string containing `node`'s value, an empty parentheses pair, and `r`. If not, we simply return the concatenation of `node`'s value, `l`, and `r`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the number of nodes in the tree rooted at `root`. We traverse the tree using DFS, which takes $O(|E|+|V|)$ time to complete. The given tree has $n$ nodes, and because it is a binary tree there can be $O(2n)$ edges at most. Hence the overall time complexity is $O(|E|+|V|) = O(2n+n) = O(n)$. The space complexity is also $O(n)$ due to the recursion stack. The tree is not guaranteed to be balanced, and thus the recursion depth can be at most $n$ deep.  
  

