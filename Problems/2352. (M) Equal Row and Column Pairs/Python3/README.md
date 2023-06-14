## 2352. (M) Equal Row and Column Pairs

### `solution.py`
The naïve method would be to check every column against each row, which would take $O(n\cdot (n+n^2)) = O(n^3)$ time since we first need to read the entire row ($O(n)$), then read all columns sequentially($O(n^2)$). This is performed for every row in `grid`, which there are $n$ of. We can do much better by utilizing dictionaries, where the key is a string representation (delimited by `.`) of a row or column and the value is the number of occurrences in its respective domain (row or column). As we only want the number of identical row-column pairs we do not need to remember which row or column were identical, hence we simply keep a counter for each unique string representation. Once the row and column dictionaries have been generated, we simply check whether each key in `row` exists in `col` and take the sum of the product of the two values if they exist.  

#### Conclusion
This solution takes $O(n^2)$ time to run, where $n$ is the dimension of `grid`($n\times n$ matrix). `grid` is iterated over twice while generating the dictionaries `row` and `col`, and the following counting step iterates over the keys of `row` once, of which there are $O(n)$ of. The space complexity is $O(n^2)$.  
  

