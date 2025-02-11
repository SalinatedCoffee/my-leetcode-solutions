## 3160. (M) Find the Number of Distinct Colors Among the Balls

### `solution.py`
There are `limit + 1` balls, initially uncolored and uniquely labeled with the integers in `[0, limit]`. The 2D list `queries` is a list of queries, where the result of some query `queries[i]` should be the number of unique colors painted onto the balls after **coloring over** the `queries[i][0]`-th ball with the color `queries[i][1]`.  
Upon reading the problem description we can see that we can solve the problem using 2 dictionaries. One will keep track of the color of each ball, and one will keep track of the number of balls painted in each color. We can then simulate the problem by iterating over `queries`, applying the coloring and then determining the result of that query. At any moment in time, the number of key-value pairs in the dictionary that maps colors to the number of balls corresponds to the number of unique colors. For each query, the coloring is performed first by updating the appropriate value in the dictionary. If the ball is already colored, we also need to update the count for the previous color, removing the entry if the color would have a frequency of `1` after painting over the ball. Once the painting is complete, we simply append the size of the appropriate dictionary to the list of query results.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `queries`. The entirety of `queries` is iterated over, and since a single query takes $O(1)$ time to process, answering all queries will require $O(n)$ time to complete. The space complexity is $O(m)$, where $m$ is `limit`. There can be at most $m$ unique colors(when each ball has a unique color), which means that the dictionaries `config` and `colors` will each contain $O(m)$ key-value pairs.  
  

