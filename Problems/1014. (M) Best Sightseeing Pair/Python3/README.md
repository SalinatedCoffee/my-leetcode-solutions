## 1014. (M) Best Sightseeing Pair

### `solution.py`
Given the list of integers `values`, we are asked to determine the maximum score of a pair of elements. The score of the pair of elements with index `i` and `j`(where `i < j`) is computed by evaluating the expression `values[i] + values[j] - (j - i)`. That is, the score of a pair of elements is the sum of their values minus the distance between the two elements.  
When we study the calculation of the score, we can rewrite it as `values[i] + values[j] - j + i`. Upon ideation, we notice that the position of element `i` effectively adds to the pair score as opposed to `j`.  

#### Conclusion
\<Content\>  
  

