## 953. (E) Verifying an Alien Dictionary

### `solution.py`, `solution_cleanup.py`
This is a pretty straightforward problem, where we first generate a mapping from the normal alphabet to the one described in `order`. Then we simply iterate through `words` while [lexicographically comparing](https://en.wikipedia.org/wiki/Lexicographical_order) two adjacent words. During each comparison, we may move on to the next pair early as soon as we encounter a character pair where the character from the previous word is smaller than the one from the next word. We can also return `False` early when we run into the opposite situation. When the words are not of the same length and we find matching character pairs up to index `min(len(words[i]), len(words[i+1]))`, the word with the *shorter* length is lexicographically smaller, so we may also decide whether to return `False` early here.  
  
#### Conclusion
The time complexity for this solution is $O(mn)$, where $m$ is the length of a word in `words` and $n$ is the number of words. The comparison step takes $O(m)$ time, and we perform this comparison $O(n)$ times. In terms of space the algorithm uses $O(1)$ space since we only keep a mapping between the alphabets in memory.  
  
