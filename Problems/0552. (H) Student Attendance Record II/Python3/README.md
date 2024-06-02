## 552. (H) Student Attendance Record II

### `solution.py`
The most straightforward way of approaching a problem like this one is to simply try all possible combinations. A brute force solution however, while correct, will most likely fail with TLE. We can speed up the algorithm significantly by memoizing intermediate results in memory, which will allow us to avoid performing redundant computation.  
In order to determine the number of possible attendance records for `d` number of days, we need 2 pieces of additional information. We need to know the current total number of absent days `a`, and the number of the current consecutive late days `l`. Naturally, each state in our recurrence relation will be represented by 3 parameters `d`, `a`, and `l`. The function `recurse(d, a, l)` will return the number of attendance records for `d` days when there are `a` absent days total and `l` consecutive late days currently. When `recurse` is called we first check whether the current state is valid by checking the values of `a` and `l`. If either `a >= 2` or `l >= 3`, then the current state cannot exist and we return `0`. We then check if the number of days to consider. If `d == 0` we return `1` since there is only one way to form an attendance record which is simply the empty string. Otherwise we try all possible choices and return the sum modulo `10**9 + 7`, with the choices being: counting the current day as being present(`P`, `recurse(d-1, a, 0)`), or as being absent(`A`, `recurse(d-1, a+1, 0)`), or as being late(`L`, `recurse(d-1, a, l+1)`). By definition of `recurse`, we want the return value of `recurse(n, 0, 0)`, which we can directly return.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is `n`. Each state in the recurrence relation is represented by 3 parameters, with one being bound by $n$, one by $2$, and one by $3$. Hence there are $6n$ states in total, with each state taking $O(1)$ time to compute. Since the values of each and every state is kept in memory, the space complexity is also linear.  
  
