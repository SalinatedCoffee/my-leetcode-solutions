## 645. (E) Set Mismatch

### `solution.py`
The most basic and straightforward approach would be to simply count the occurrences of each value in `nums`. We could implement this algorithm with a set, but we can also do so with a simple list by taking advantage of the fact that `nums` is densely populated. Once all values in `nums` have been examined, we return a list where the first element is that in `nums` that appears twice and the second is the one that does not appear at all.  

#### Conclusion
The time and space complexity for this solution is $O(n)$, where $n$ is the length of `nums`. `nums` and `freq` are both $n$ long and are iterated over exactly once. For both iterations, processing a single element takes constant time, hence the overall time complexity of $O(n)$.  
  


### `solution_2.py`
We can also solve this problem with a little bit of math. Because `nums` contains *all* values from `1` to `len(nums)` except for one number that is duplicated, we can easily compute the difference between the sum of `nums` and the 'ideal' sum of the integers from `1` to `len(nums)`. Just this value alone is not enough however, as the difference could happen at any value. For example, the lists `[1, 1, 3, 4]` and `[1, 2, 2, 4]` have the same sum and consequently the same difference. In order to identify the duplicated value we need to also compute the sum of the squared integers. The closed formula of this sequence is $n(n+1)(2n+1)/6$. We can now derive the duplicated number through some basic algebra.  
Let the difference between the ideal sum and actual sum ($\text{ideal}-\text{actual}$) be $d$, the difference between the ideal squared sum and actual squared sum be $d_{sq}$, the duplicate integer be $x$, and the missing integer be $y$. It is not that difficult to reason that $y - x = d$, and by extension, $y^2 - x^2 = d_{sq}$. $d$ and $d_{sq}$ is known, and we want to solve for $x$. Rearranging the first equation to get $y = x + d$, we can plug this into the second equation to get $(x + d)^2 - x^2 = d_{sq}$. Expanding, we get $x^2 + 2dx + d^2 - x^2 = d_{sq}$. If we clean this up and rearrange for $x$, we get $x = (d_{sq} - d^2) / 2d$. We can easily compute the value of $x$ using this formula, and computing the value of $y$ based on $x$ is also trivial.  



#### Conclusion
This solution has a time complexity of $O(n)$. We still need to compute the sum and squared sum of `nums`, which takes $O(n)$ time to complete. The space complexity is $O(1)$ as only a handful of integers are used to store relevant values.  
  

