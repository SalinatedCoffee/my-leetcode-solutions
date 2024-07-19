## 1380. (E) Lucky Numbers in a Matrix

### `solution.py`
Given a 2D list `matrix` that contains only unique positive integers, we are asked to return a list of elements in `matrix` that are the smallest in their row and largest in their column. If no such element exists, an empty list should be returned. We can easily solve this problem by preprocessing each column and comparing that value to the minimum value of each row. Upon further examination of the problem however, we can see that only 1 valid element can exist in `matrix`. In order to prove this, we will first assume that there are more than 2 valid elements in `matrix` as follows:  
$$
\begin{bmatrix}
L_1 & \cdots & N_1 \\
\vdots & \ddots & \vdots \\
N_2 & \cdots & L_2
\end{bmatrix}
$$
Where $L_1$ and $L_2$ are the valid elements, and $N_1$, $N_2$ arbitrary invalid elements. According to the problem description, we know that $N_2 < L_1 < N_1$ and $N_1 < L_2 < N_2$. However the inequalities suggest that $N_1 < N_2$ *and* $N_1 > N_2$, which is clearly impossible. Hence, we can say that our initial assumption of there being more than 2 valid elements is false, and `matrix` can have exactly 1 valid number as specified by the problem.  
While the proof does not drastically change the actual solution implementation, we can now return immediately whenever a valid element is found. The rows are first processed into `row_min`, where the value of `row_min[i]` is the minimum value of the `i`th row. `matrix` is then iterated over column-by-column, returning immediately whenever the maximum of the column is also the minimum value of its row. If the iteration completes without returning, then `matrix` has no valid element and we return an empty list.  

#### Conclusion
This solution has a time complexity of $O(mn)$ where $m$ and $n$ are the number of rows and columns of `matrix`, respectively. Preprocessing the rows of `matrix` as well as the column-wise iteration that follows each take $O(mn)$ time to complete, hence the overall time complexity of $O(n)$. The space complexity is $O(m)$ due to the list `row_min`.  
  

