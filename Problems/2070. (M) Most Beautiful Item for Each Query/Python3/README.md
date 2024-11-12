## 2070. (M) Most Beautiful Item for Each Query

### `solution.py`
The 2D list `items` contains lists of length 2 that represents a single item. `items[i][0]` and `items[i][1]` each represent the price and beauty of the `i`th item, respectively. Given the list of integers `queries`, we are asked to return a list of results after evaluating each query. A single query on an integer `q` should return the maximum beauty of an item that has a price of at most `q`. We can immediately see that we could sort the items in ascending order of a price and precompute the maximum beauty of each prefix. This way we can efficiently retrieve the maximum beauty given a price by running binary search on the prices. The problem is that there may be multiple items with the same price, which means that computing the prefix maximum beauty for each item will fail in such cases. To solve this problem we can compute prefix maximum beauties for each unique price instead of items, which we can do by using a dictionary.  
`items` is first sorted in ascending order of price. The dictionary `items_unique` is initialized as a `defaultdict(int)`, and will contain the maximum beauty of an item with a price of at most each unique price in `items`. For example, if `items = [[1, 2], [1, 5], [2, 3]]`, the contents of `items_unique` will be `{1: 5, 2: 3}`. The key-value pairs are then extracted from `items_unique` as tuples, and are again sorted in ascending order of price(though this may not be necessary as dictionaries remember the insertion order of each key-value pair) before being assigned back to `items_unique`. We can now start processing the list of queries, using Python's `bisect` module to perform binary search on the sorted list of tuples. A query is invalid only if the input is less than the smallest unique price; in which case we append a `0` to the list or results as instructed. Otherwise, we take the tuple at the index returned from the binary search step and append the beauty to the list of results.  

#### Conclusion
This solution has a time complexity of $O((n+m)\log n)$, where $n$ is the length of `items` and $m$ is the length of `queries`. Preprocessing `items` involves sorting `items` in ascending order of price($O(n\log n)$, iterating over it while populating a dictionary($O(n)$), and sorting the key-value pairs of said dictionary in ascending order of keys($O(n\log n)$). The query processing step that follows involves processing each and every query in `queries`, with each query taking $O(\log n)$ time to answer using binary search on the sorted list of tuples `items_unique`. Hence, the overall time complexity comes out to be $O(n\log n + m\log n) = O((n+m)\log n)$. The space complexity is $O(n)$, due to the sorting step, intermediate dictionary, and list of tuples `items_unique`.  
  
