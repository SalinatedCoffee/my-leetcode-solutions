## 1014. (M) Best Sightseeing Pair

### `solution.py`
Given the list of integers `values`, we are asked to determine the maximum score of a pair of elements. The score of the pair of elements with index `i` and `j`(where `i < j`) is computed by evaluating the expression `values[i] + values[j] - (j - i)`. That is, the score of a pair of elements is the sum of their values minus the distance between the two elements.  
When we study the calculation of the score, we can rewrite it as `values[i] + values[j] - j + i`. Looking at the rearranged expression, we notice that the position of element `i` effectively only adds to the pair score as opposed to `j`. This means that given a fixed element `j`, the element `i` that would yield the highest score when paired with `j` is simply the largest element in the prefix array `values[:j]`. This means that we can scan through `values` from the left towards the right while keeping track of the element with the highest score up to the current point in time. Then, we can trivially compute the largest score achievable by using the current element as element `j`. Among all of these values, we need only select the largest value and return it.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `values`. `values` is iterated over exactly once, and since each value takes $O(1)$ time to process, the entire iteration will complete in $O(n)$ time. The space complexity is $O(1)$.  
  

