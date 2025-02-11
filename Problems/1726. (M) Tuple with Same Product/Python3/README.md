## 1726. (M) Tuple with Same Product

### `TLE.py`
Given the list of **unique** positive integers `nums`, we are asked to count the number of quadruples `(a, b, c, d)` that satisfy the following conditions:  

- `a * b == c * d`  
- `a != b != c != d`  

We see that the second condition is always satisfied whenever the first condition is, since `nums` only contains unique values. We also notice that 8 unique quadruples can be formed when given a set of 4 values in `nums` that satisfy both conditions due to the property of multiplication. 2 permutations exist for *each* side of the equation(`a * b` is equivalent to `b * a`), and the equation itself has 2 permutations as well(`lhs == rhs` is equivalent to `rhs == lhs`). Therefore, the full equation involving all 4 terms will have `2*2*2 = 8` permutations total. This means that we can determine the total number of valid quadruples if we know the number of sets of 4 values that satisfy the first condition.  
We can exploit a few properties of a valid quadruple to search for valid sets of 4 values. First off, we can rearrange the first condition for `d`(or any other term) into the form `a * b / c == d`. Through this expression we can see that `a`, `b`, and `c` **cannot** be in the same set if `a * b` is not a multiple of `c`. If it is, a valid set can be formed if `nums` contains `a * b / c`. Another property of the first condition is that if `a` and `b` are both strictly larger(or smaller) than `c` and `d`, the expression must evaluate to `False`.  
A brute force solution can be implemented by utilizing the above observations. We know that we need to fix 3 values in order to determine whether a valid set can be formed. We also know that the terms on one side of the equality must not be strictly greater than or less than the terms on the other side. If `nums` is sorted, we can avoid such cases by fixing `a` and `b` with the first and last element of `nums` and moving inwards. Then, `c` can be fixed using any value between `a` and `b`.  
`nums` is first sorted in ascending order. We then nest 2 for loops, with the outer loop iterating over `nums` from the left towards the right and the inner loop from the right towards the left. The product of the two values are computed, after which an empty set is initialized. This set will contain the values found between the two elements from the for loops. Yet another for loop is added, iterating over the elements between the two from the 2 outer loops. If the product is a multiple of the current element of the innermost loop, we compute the quotient and determine whether it exists within `nums` by consulting the set of seen values. If it exists, we increment the counter by `8`. The current element of the innermost loop is added to the set before moving on to the next value.  

#### Conclusion
This algorithm has a time complexity of $O(n^3)$, where $n$ is the length of `nums`. `nums` is iterated over for each loop inside a triply nested for loop, and each element takes $O(1)$ time to process. Sorting `nums` takes $O(n\log n)$ time, bringing the overall time complexity to $O(n^3 + n\log n) = O(n^3)$. The space complexity is $O(n)$, due to the sorting step and set `cand`.  
  

### `solution.py`
We can devise a more efficient solution by realizing the fact that we can simply count the pairs by the value of their product. If we consider each side in the equality of the first condition as one term, the expression simply becomes `p1 == p2`. If we know the number of pairs that have `p1`(or `p2`) as their product, we can trivially count the number of `p1` and `p2` pairs that satisfy the condition. From this value, we can also trivially compute the number of permutations by multiplying it by `8`.  
A dictionary is used to keep track of the number of pairs for each pair product. The dictionary is populated by simply examining all possible pairs of values in `nums`, computing the product of the pair and updating the appropriate value in the dictionary. Then, we iterate over all unique values in the dictionary, computing the number of permutations and adding it to the total count.  

#### Conclusion
This solution has a time complexity of $O(n^2)$. Unlike the previous attempt, this solution only has a singly nested for loop, bringing the overall time complexity down by a magnitude of $n$. Since there can be $O(n^2)$ unique products, the counting step requires $O(n^2)$ time to complete as well. The space complexity is also $O(n^2)$, due to the dictionary `prods`.  
  

