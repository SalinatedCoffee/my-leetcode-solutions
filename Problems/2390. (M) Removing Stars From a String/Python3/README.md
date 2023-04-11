## 2390. (M) Removing Stars From a String

### `solution.py`
We want to remove *all* stars from the given string `s`. Thankfully, the problem constraints state that a remove operation is always possible, and so we do not have to consider cases where we encounter a `*` when there are no letters to delete. The operation involves removing a `*` and the closest letter on its *left*. We could iterate along the left until a letter is found then remove that letter, but since strings are immutable in Python that would slow things down considerably. Instead we can maintain a stack of letters to be removed, since that would naturally let us remove the most recent (that is, the *first* character to the *left* of the current `*`) deletable letter in optimal time.  
Thus we can iterate across `s` while pushing all letters into `stack` and popping a letter off of `stack` whenever a `*` is encountered. After the iteration has finished we may simply concatenate the contents of `stack` and return the resulting string.  

#### Conclusion
The time complexity is $O(n)$ where $n$ is the length of `s`. We iterate across `s` once, and we either `pop()` or `push()` on `stack` which takes constant time. The space complexity is also $O(n)$ as `stack` can at most contain all characters in `s`.  
  

