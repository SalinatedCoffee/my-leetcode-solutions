## 3042. (E) Count Prefix and Suffix Pairs I

### `solution.py`
Given the list of strings `words`, we are asked to return the number of valid pairs of elements. A pair is considered valid when `words[i]` is both a prefix and suffix of `words[j]`, for the pair of elements `words[i]` and `words[j]` where `i < j`. Looking at the problem constraints, we know that we can trivially solve the problem by taking a brute force approach that examines all possible pairs of elements in `words`.  
We first define the helper function `is_prefix_and_suffix`, which takes 2 strings `candidate` and `target`. If `candidate` is a prefix and a suffix of `target` the function returns `True`, and `False` otherwise. `words` is then iterated over using nested for loops, incrementing the number of valid pairs `res` by `1` if `is_prefix_and_suffix` returns `True` for the current pair of strings.  

#### Conclusion
This solution has a time complexity of $O(n^2m)$, where $n$ is the length of `words` and $m$ is the average length of the strings in `words`. There are $O(n^2)$ total pairs of elements in `words`, all of which are examined. Validating a given pair requires $O(m)$ time, hence the overall time complexity of $O(n^2m)$. The space complexity is $O(m)$ because in `is_prefix_and_suffix`, `target` is sliced in order to generate the prefix and suffix to compare against `candidate`. Since slicing a string creates a new string containing the characters of the relevant section of the original string, validating a pair of strings will use $O(m)$ memory.  
  

