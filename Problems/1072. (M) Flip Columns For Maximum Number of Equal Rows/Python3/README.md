## 1072. (M) Flip Columns For Maximum Number of Equal Rows

### `solution.py`
We are allowed to 'flip' an arbitrary set of columns in the binary `m` by `n` 2D list `matrix`. Our task is to determine the maximum number of rows that contain identical elements after the columns are flipped. Because `matrix` is a binary list, we know that there is no point in flipping a column more than once. We can also visualize flipping the `i`th column as XORing a value with the `i`th bit raised with each and every row represented as a binary number. If we were to flip the `0`th, `3`rd, and `4`th columns, for example, the resulting rows would be each row XORed with the binary value `0..011001`. It can also be said that if a row is the compliment of another row, **both** rows can be made valid by flipping the same set of columns since a valid row can contain either only `0`s or `1`s. As the constraints on the size of `matrix` is relatively small, we can brute force the problem by selecting each row and counting the number of rows in `matrix` that are either identical to the row itself or its compliment.  

#### Conclusion
This solution has a time complexity of $O(m^2 n)$ where $m$ is the number of rows and $n$, the number of columns in `matrix`. Comparing a row to another row requires $O(n)$ time to complete. Consequently, searching `matrix` for a single row(as well as its compliment) will finish in $O(mn)$ time. As there are $m$ rows in `matrix`, the overall time complexity will be $O(m^2 n)$. The space complexity is $O(n)$, as we temporarily keep the complement of a row in memory as `matrix` is searched.  
  

