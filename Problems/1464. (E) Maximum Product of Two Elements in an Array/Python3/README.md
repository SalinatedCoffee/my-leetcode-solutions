## 1464. (E) Maximum Product of Two Elements in an Array

### `solution.py`
Since the input size is small enough, the obvious solution is to try all possible pairs of integers in `nums`. Using a nested for loop we can compute `(nums[i]-1) * (nums[j]-1)` for all possible indices `i` and `j` (where `i != j` of course) and return the largest value.  

#### Conclusion
This solution has a time complexity of $O(n^2)$ where $n$ is the length of `nums`. There are $n^2 - n$ valid integer pairs in `nums`, and we examine every one of them. The space complexity is $O(1)$.  
  


### `solution_2.py`
Because the values in `nums` are guaranteed to be non-negative, the largest possible product of an integer pair in `nums` is simply the product of the largest and the second-largest values. If we sort `nums`, we can trivially retrieve these values, after which we can compute the desired value.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$. `nums` is sorted once, which takes $O(n\log n)$ using Python's built in `list.sort()`. The space complexity is $O(n)$, also due to the sorting step.  
  


### `solution_3.py`
Instead of sorting, we can simply iterate along `nums` to find the largest and second-largest values. We keep track of 2 integers `a` and `b`, which are the largest and second-largest elements in `nums` respectively. If some value in `nums` is larger than `a`, we set `b` to `a` and `a` to `nums`. Otherwise, we assign `nums` to `b` accordingly.  

#### Conclusion
This solution has a time complexity of $O(n)$. `nums` is iterated over once, and only a handful of constant time operations are performed for each element in `nums`. The space complexity is $O(1)$.  
  

