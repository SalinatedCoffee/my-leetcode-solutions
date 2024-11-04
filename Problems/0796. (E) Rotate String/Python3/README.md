## 796. (E) Rotate String

### `solution.py`
Given the strings `s` and `goal`, we are asked to determine whether `s` can be rotated towards the left to form a string equal to `goal`. If `goal` *can* be formed by rotating `s`, we can say that some integer `i` exists where `s[i:] + s[:i] == goal` and `0 <= i <= len(s)`. That is, `goal` can be formed by splitting `s` at some position into a prefix and suffix and then appending the *prefix* after the suffix. We can easily brute force this by using Python's slice functionality, running through each position of `s` where a split can be performed and comparing the resulting rotated string against `goal`. If a match is found, we can immediately return `True`. Otherwise, we return `False` after the loop exits normally.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is the length of `s`. There are $n$ possible split positions, and each position is evaluated by generating the string rotated to that position and comparing it against `goal`. Since each of these operations require $O(n)$ time to complete, the overall time complexity of this solution comes out to be $O(n^2)$. The space complexity is $O(n)$, as each rotated string is briefly kept in memory while it is compared against `goal`.  
  

