## 1572. (E) Matrix Diagonal Sum

### `solution.py`
Essentially, we want to access all elements in a X-pattern in the given matrix. We can achieve this by simply iterating over the rows of `mat` while taking the sum of the first and last elements for the first row, the second and second-to-last elements for the second row, and so on. We could use two pointers to keep track of which elements to access, but we notice that the two column indices also increase/decrease by 1 in accordance with the row index. We can also cut the number of iteration in half by recognizing that the matrix is square, which allows us to trivially retrieve the elements in a horizontally symmetric fashion. Once the loop has exited we need to check whether the matrix has odd-sized dimensions in order to determine whether the center element needs to be fetched or not.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `mat`. We iterate over half the rows of `mat` only once, hence the linear time complexity. The space complexity is $O(1)$.  
  

