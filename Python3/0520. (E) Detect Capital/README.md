## 520. (Easy) Detect Capital

### `solution.py`
Not really sure what to talk about this one. We do a sanity check for when the word is one letter long, in which case the word is always properly capitalized. After, we compare a letter to the preceding one and check whether the capitalization differs - with the exception of the first two letters.
#### Conclusion
This solution runs in $O(n)$ time, where $n$ is the length of the word.
