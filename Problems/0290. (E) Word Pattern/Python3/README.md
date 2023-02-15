## 290. (Easy) Word Pattern

### `solution.py`
The length of the pattern and number of words are not guaranteed to be equal, so we do a quick sanity check before doing anything. Then, we iterate through both the pattern and words and keep track of valid mappings in a dictionary using the pattern symbol as the key and word as the value. If a key is in the dictionary, we return `False` if the dictionary value and current word does not match. If a key is not in the dictionary, we return `False` if the current word is already in the dictionary.
`True` is returned when the loop exits normally.

#### Conclusion
This solution runs in $O(n)$ time, where $n$ is the length of the pattern.
