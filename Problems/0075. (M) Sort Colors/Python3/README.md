## 75. (M) Sort Colors

### `solution.py`
The easy solution is to simply perform a counting sort on `nums`. Since there are only 3 types of 'colors' in `nums`, we can initialize an empty list of length 3 with `0`s. We make an intial pass over `nums` while counting each color in the frequency list. Then we make a second pass over `nums`, overwriting it with colors according to the frequency counts from earlier.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `nums`. `nums` is iterated over twice, with each round of traversals taking $O(n)$ time to complete. The space complexity is $O(1)$, as we only use a single list of fixed length.  
  

