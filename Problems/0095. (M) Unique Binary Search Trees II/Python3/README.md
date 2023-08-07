## 95. (M) Unique Binary Search Trees II

### `solution.py`

Given an integer `n`, we want to generate all unique binary search trees that contain the nodes from `1` to `n`. Since we are working with binary *search* trees, we can also interpret this as simply generating every possible binary search trees with `n` nodes, without duplicates. We can easily solve this problem through a top-down dynamic programming approach. If we are given some range of nodes, say from `l` to `h`, we know that each node within that range can be a candidate to be the root. If we select a node `i` as the root, all nodes in the range `[l, i-1]` are smaller than `i`, and those in the range `[i+1, h]` are larger than `i`. We want all possible binary search trees for this configuration, so it stands to reason that all possible BSTs with nodes in the range `[l, i-1]` should be the left child of `i`, and vice versa. At this point, we can clearly see that we can recursively apply this algorithm to the ranges `[l, i-1]` and `[i+1, h]` to generate all possible BSTs from them.  

Now that we have a recursive algorithm that generates all unique BSTs for a range of integers, we can see that the recursive function can be called multiple times with the same parameters. The return value given some parameters can be trivially memoized using the built-in decorator `@cache`.  

#### Conclusion

This solution has a time complexity of $O(4^n\cdot n^{-0.5})$, where $n$ is `n`. The number of unique BSTs that contains `n` nodes is what is known as a [Catalan number]([Catalan number - Wikipedia](https://en.wikipedia.org/wiki/Catalan_number#Applications_in_combinatorics)), where the `n`th Catalan number is defined as $4^n\cdot n^{-1.5}$. Each BST takes $O(n)$ time to generate since they contain `n` nodes, hence the overall time complexity of $O(4^n\cdot n^{-1.5}\cdot n) = O(4^n\cdot n^{-0.5})$. As is the case for these types of problems, the space complexity is not easy to analyze.  


