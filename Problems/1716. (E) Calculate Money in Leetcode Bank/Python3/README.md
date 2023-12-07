## 1716. (E) Calculate Money in Leetcode Bank

### `solution.py`
We can simply simulate the problem by generating a list with the deposit amount for each day, and computing the sum of that list. The amount deposited each day can be thought of as two components. One component is the base amount, which is simply the number of the current week(0-indexed). This can be trivially computed by using integer division. The other component is the additional amount, which we can also easily compute by taking the modulo `7` of the current day. If we arbitrarily count the number of days starting from `0`, we also need to add `1` to account for this decision.  
The list can be easily generated using Python's list comprehension, the sum of which we can directly return.  

#### Conclusion
The time and space complexity of this solution is $O(n)$, where $n$ is `n`. A list of length $n$ is generated that contains the deposit amount of each day. We then compute the sum of this list and return it.  
  


### `solution_2.py`
Because the deposit pattern is simple enough, we can directly calculate the sum instead of simulating the daily deposits. Again, we think of a deposit as having two components. Then the base amount does not change through the week, while the additional amount keeps increasing by `1` until the end of the week, after which it resets back to `1`. The sum of the additional amounts for a week is identical across different weeks. We can first calculate the deposit sum for `i` **full** weeks in `n`, and then compute the deposit sum for the remaining days. If there are `j` days left over, the base amount is the number of full weeks + 1 multiplied by `j`. The additional amount is `j*(j+1)//2`. Once we have finished calculating the sums for each component, we can simply add them and return that value.  

#### Conclusion
This solution has a time and space complexity of $O(1)$(assuming modulo and division operations take constant time).  
  

