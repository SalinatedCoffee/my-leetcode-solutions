## 2028. (M) Find Missing Observations

### `solution.py`
There is a 6-sided die, rolled `m + n` times. `m` rolls have been observed, with each roll recorded in `rolls`. `n` rolls have not been observed, but the arithmetic mean of all `m + n` rolls is given as the integer `mean`. Given `rolls`, `n`, and `mean`, we are asked to return a *list* of all `n` unobserved rolls.  
Thankfully, we are given enough information to simply compute the values of unobserved rolls. The equation for computing the arithmetic mean of all dice rolls is  
$$
\frac{tot_{all}}{m + n} = avg_{all}
$$
Where $tot_{all}$ is the sum of all dice rolls and $avg_{all}$ is `mean`. $tot_{all}$ can be rewritten as the sum of the sum of non-observed rolls($tot_n$) and sum of observed rolls($tot_m$). As the value of the latter is known, we can compute the sum of all non-observed rolls through the equation $tot_n = (m+n)avg_{all} - tot_m$, which is `tot_n = (m + n) * mean - sum(rolls)`. Now that we know the sum of all unobserved rolls, as well as the number of rolls, we can 'distribute' the sum over `n` dice rolls. One thing to notice here is because the dice is a traditional 6-sided die, a single roll can have a minimum value of `1` and a maximum value of `6`. Hence, performing `n` rolls of this dice can yield a minimum total value of `n` and a maximum value of `n*6`. If `tot_n` is outside of this range, it is impossible to get a sum of `tot_n` by rolling the dice exactly `n` times, and we should be returning an empty array. Otherwise, we first evenly 'distribute' the sum over `n` rolls and arbitrarily spread the remainder. How the sum is distributed does not matter as long as the value of each roll lies within the interval `[1, 6]`.  


#### Conclusion
This solution has a time complexity of $O(m+n)$ where $m$ is the length of `rolls` and $n$ is `n`. `sum(rolls)` requires $O(m)$ time to complete, and the initialization of `res` takes $O(n)$ time - bringing the overall time complexity to $O(m+n)$. The space complexity is $O(1)$, excluding the returned list `res`.  
  

