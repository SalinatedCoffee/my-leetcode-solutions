## 633. (M) Sum of Square Numbers

### `solution.py`
We are asked to determine whether the integers $a$ and $b$ exist for the expression $a^2 + b^2 = c$, where $c$ is given as the non-negative integer `c`. While `c` can be very large, a linear scanning approach is still viable as we are looking for the root of a variable bound by `c`, which reduces the search space significantly. We simply iterate over the interval `[1, int(sqrt(c))+1)` while checking whether the square root of `c` subtracted by the square of the current value is an integer. If it is, we immediately return `True` as the problem asks us to determine whether the integers $a$ and $b$ exist.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is `c`. The candidates for $a$ are in the interval `[1, int(sqrt(c))+1)` and evaluating each candidate takes $O(1)$ time to complete(assuming Python's `sqrt()` takes $O(1)$ time to compute), bringing the overall time complexity to $O(n)$. The space complexity is $O(1)$.  
  

