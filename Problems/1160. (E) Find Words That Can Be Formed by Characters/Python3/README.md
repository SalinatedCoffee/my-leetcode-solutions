## 1160. (E) Find Words That Can Be Formed by Characters

### `solution.py`
For this problem, we can take a brute force approach that evaluates the 'goodness' of each string in `words`. As each character in `chars` can only be used once, we need to keep track of the frequency of each letter as well. Python's built-in `Counter` object is perfect for this purpose, as it uses a dictionary under the hood and automatically handles the counting for us. We first initialize a `Counter` `bl_char` which will serve as our 'baseline'. Iterating over each word in `words`, we initialize another `Counter` using that word and evaluate it against `bl_char` using `w_cmp()`. `w_cmp()` simply checks every character in the given word against `bl_char`, and returns `False` whenever a character is not in `bl_char`, or there are more characters in the word. If `w_cmp()` evaluates to `True`, we increment `ret` by the length of the current word. Once every word has been examined, we may simply return `ret` directly.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ is the average length of the words in `words` and $n$ is the length of `words`. There are $n$ words total, and each word is used to instantiate a `Counter()` object, which takes $O(m)$ time. The space complexity is $O(m+k)$, where $k$ is the length of `chars`.  
  

