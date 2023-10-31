## 792. (M) Number of Matching Subsequences

### `solution.py`
Because we are asked to verify whether a word in `words` is a subsequence of `s`, we can think of `s` as a superset of a word in `words`. As such, we can greedily match pairs of characters while iterating over both `s` and a word to determine whether the word is a subsequence of `s`. Say we want to verify whether `word` is a subsequence of `s`. While iterating over `s`, we check whether the current character of `s` matches that of the current character in `word`. If so, we advance the pointer of `word` by `1` and move on to the next character of `s`. If the `word` pointer ever reaches the end, it means that all characters in `word` has been matched to those in `s`, and thus `word` is indeed a subsequence of `s`. On the other hand, if the end of `word` has not been reached after `s` has been iterated across, it means that some characters in `word` were not able to be matched and so `word` is not a subsequence of `s`.  
We can generalize these steps for multiple words, by 'simultaneously' matching character pairs over all words in `words`. To do this, we need a way to quickly access words starting with a certain character. Using a list with `ord()` to translate characters into indices is certainly possible, but here we will simply use dictionaries as it greatly simplifies the code with little hashing overhead. The dictionary `l2w` is first initialized by iterating over `words` and inserting a word in the appropriate list. Then we start iterating over `s`, retrieving the list of words that start with a character in `s` via `l2w`. For a list of words we match the first character of each word by removing it from a word and adding that word back to `l2w` based on its new first character. If a word only consists of 1 character, that means that that word has been fully matched and is a subsequence of `s` - and we increment `ret`, which is simply a counter for the number of subsequences in `words`.  
Once the entierety of `s` has been iterated over, we can simply return `ret`.  

#### Conclusion
The time complexity for this solution is $O(m+n)$, where $m$ is the length of `s` and $n$ is the sum of the lengths of all words in `words`. We effectively iterate over `s` and all words in `words` simultaneously, and the worst case is when all words in `words` are identical to `s` - hence the time complexity of $O(m+n)$. The space complexity is $O(k)$, where $k$ is the length of `words`. `l2w` can at most contain a tuple for each word in `words`, and as such will use $O(k)$ memory.  
  
