## 1582. (E) Special Positions in a Binary Matrix

### `solution.py`
The brute force solution would involve checking the row and column for each element. This approach is obviously inefficient, as it ends up counting `1`s multiple time for the same row or column. We can instead precompute the number of `1`s in a row or column in lists `row` and `col`. Then we iterate over `mat` again, checking the values of `row[i]` and `col[j]` whenever `mat[i][j]` is `1`. If `row[i]` and `col[j]` are also `1`, it means that `mat[i][j]` is indeed a special position.  

#### Conclusion
This solution has a time complexity of $O(mn+mn) = O(mn)$ where $m$ and $n$ are the dimensions of `mat`. We iterate over every element in `mat` 2 times; once during the preprocessing step, and once to count the number of special positions. The space complexity is $O(m+n)$, as we keep the number of `1`s in each row and column in memory.  
  


### `solution-tweaked.py`
We can rearrange the special position step for a slight running time reduction. The implementation in the previous step indexes into `mat` $mn$ times. This is unnecessary however, as `mat[i][j]` can only be special if `row[i]` and `col[j]` are also `1`. By checking `row` and `col` first we can avoid having to index into `mat` on certain occasions.  
In the first solution we accessed `mat` first, then `row`, and finally `col`. If we examine the conditional we can see that `mat` is always accessed. In the rearranged version only `row` is always accessed, which is an improvement in running time as `row` is always smaller than or equal to `mat`.  
  
#### Conclusion
The time and space complexity of this solution is identical to the first solution. The improvement in time complexity are in the best and average cases.  
  
