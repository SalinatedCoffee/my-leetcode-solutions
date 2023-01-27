## 472. (H) Concatenated Words

### `solution.py`
Intuition tells us that we can use a [trie](https://en.wikipedia.org/wiki/Trie) containing all given words to check whether a substring of a word exists in the provided `words`. The naive implementation of a trie is relatively simple, so we won't go over the details here. Now we need to figure out a way to check if a word is comprised of smaller words in the given word list. If a substring of a word is not in the word list, all substring partitionings containing that specific substring cannot possibly be a valid concatenation. So when iterating through a word we may skip cases where the prefix of the current substring is not a valid concatenation. We also want to avoid redundant checks of substrings, and so for every word we keep a list of length `len(word)+1` where the value at index `i` represents whether the substring `word[0:i]` is a valid concatenation or not. By doing this, we only need to iterate over a range only once since *all* valid concatenations in that range will be discovered and memoized after one pass. Once we see that the value at index `len(word)` is True, the entire word is a valid concatenation and so we may append it to a return list and move on to the next word.  
  
#### Conclusion
The time complexity of this algorithm is $O(mn)$, where $m$ is the length of a word and $n$ is the length of `words`. Insert and find operations on a trie takes $m$ time, and we perform this operation for all given words.  The space complexity is $O(26^{\log_{26}n})$ since a trie node can have at most 26 (number of lowercase characters) children.
  

### `solution_2.py`
Looking at the first solution, we realize that we can substitute the trie with any other data structure that suports inserts (without duplication) and lookups. A set supports all of the aforementioned operations, and has the added benefit of being more efficient in both runtime and memory.  

#### Conclusion
This solution runs in $O(mn)$ time, since inserting all words into a set takes $O(1*n)$ time and the validation of words takes $O(mn)$ time. The space complexity is also $O(mn)$ since `bag` may contain $n$ words of length $m$.  
  

