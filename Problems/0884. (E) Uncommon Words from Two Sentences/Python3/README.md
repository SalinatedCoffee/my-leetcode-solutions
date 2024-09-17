## 884. (E) Uncommon Words from Two Sentences

### `solution.py`
A word is considered to be 'uncommon' if it appears only once in its sentence, and does not appear in the other sentence. Given this definition and the strings `s1` and `s2`, we are asked to return the list of uncommon words in any order. This problem can easily be solved by using 2 dictionaries, with the keys being the words and values the word's number of appearances in its sentence. Since both strings are guaranteed to be 'properly' formed we can split them into their constituent words by using the `.split()` method. The list of words is then passed as the argument of a `Counter` instantiation, which will result in a dictionary with the same key-value pair configuration as described above. The last order of business is to iterate over each dictionary, appending a word to the return list `res` whenever a word has a value of `1` *and* does not exist in the other dictionary.  

#### Conclusion
This solution has a time complexity of $O(m+n)$ where $m$ and $n$ are the lengths of `s1` and `s2`, respectively. Splitting the strings, instantiating a `Counter` using the resulting list of words, and iterating over the dictionaries each take linear time with respect to the length of the strings. The space complexity is also $O(m+n)$, as both dictionaries are kept in memory until the algorithm exits.  
  

