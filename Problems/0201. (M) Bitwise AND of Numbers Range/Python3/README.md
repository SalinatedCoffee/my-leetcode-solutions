## 201. (M) Bitwise AND of Numbers Range

### `solution.py`
The brute force approach of actually ANDing every integer between `left` and `right` will take too long to run. Instead, we can exploit the properties of the bitwise AND operation to compute the AND sum much more quickly. Say we want to compute the AND sum of a list of numbers containing either `0` or `1`. As bitwise AND returns a `1` only when both operands are `1` as well, we can conclude that the AND sum can be `1` if the list does not contain any `0`s. Why does this matter? If we think about the problem as performing bitwise AND on all of the values in the interval stacked on top of each other (as we would do in grade level addition) all we have to do is identify the columns that contain at least one `0`. Now the problem becomes determining the columns that will contain a `0`. From `left` to `right`, we are bitwise ANDing all integers between them(inclusive). As a digit can only be either `0` or `1` in binary, we can say that any *changing* digits that have a `0` on their left will also be `0` at some point between `left` and `right`. For example if `left = 5`(`101` in binary) and `right = 7`(`111` in binary), we know that the 2 digits from the right are 'changing' digits as they are not identical between `left` and `right`. We also see a `0` at the second digit, so we know that the column corresponding to the first digit will contain a `0`. Hence, the AND sum of the integers between `left` and `right` will be `100` in binary, which is `4`. In summary, all we have to do is simply find the longest common prefix of `left` and `right`, and set all remaining digits to `0`.  
To achieve this, we can simply bit shift `left` and `right` simultaneously until their values are equal. Then, we shift that value towards the left until the value has the same bit length as `right`, after which we can return the value.  

#### Conclusion
This solution has a time complexity of $O(\log n)$, where $n$ is `right`. In the worst case, we shift `right` to the right until it becomes `0`, which takes $O(\log n)$ time to complete. Shifting the prefix back into a returnable value is also a $O(\log n)$ operation. The space complexity is $O(1)$.  
  
