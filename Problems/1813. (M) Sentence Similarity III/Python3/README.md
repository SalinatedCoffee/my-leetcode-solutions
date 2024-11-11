## 1813. (M) Sentence Similarity III

### `solution.py`
A 'sentence' is a string comprised of whitespaces and lower/uppercase English letters. There are no leading or trailing whitespaces, and words are separated by a single whitespace. Given the two sentences `sentence1` and `sentence2`, we are asked to return `True` if they are 'similar' to each other. Two sentences are similar if one can be formed by inserting a sentence(with empty sentences being allowed) in the other sentence. For example, sentences `"Quick lazy dog"` and `"Quick fox jumps over the lazy dog"` are similar since the sentence `"fox jumps over the"` can be inserted into `"Quick lazy dog"` to form `"Quick fox jumps over the lazy dog"`.  
First off, we can immediately see that we can split each sentence into a list of words and use the lists to determine the similarity of the sentences. One may be forgiven for coming up with a two pointer approach that iterates over both sentences while comparing pairs of words. This approach will not work however, as we do not know which pointer needs to be advanced when a word pair does not match. Instead, we can think about the properties of the sentences themselves. Assume that the given sentences are similar, and `sentence1` is longer than `sentence2`. Because they are similar, it must be the case that an arbitrary sentence can be added between two words in `sentence2` to form `sentence1`. Because only 1 sentence can be added, we can say that `sentence1` can be formed by splitting `sentence2` into two pieces and adding an arbitrary sentence between them. Simply put, if the combined length of the longest common pre/suffix between `sentence1` and `sentence2` is longer than or equal to the length of `sentence2`, the sentences are similar.  
Splitting the given strings into a list of words can be trivially accomplished through the use of `string.split()`. We then traverse both lists to determine the length of the longest common prefix, and a second time to determine the length of the suffix. If either the prefix or suffix has the same number of words as `sentence2`, `sentence1` can be formed by appending or prepending a sentence to `sentence2`, and they are similar. Otherwise, we check the length of the prefix and suffix and return `True` if the combined number of words exceeds that of `sentence2`.  
  

#### Conclusion
This solution has a time complexity of $O(m+n)$, where $m$ and $n$ is the length of `sentence1` and `sentence2`, respectively. Splitting the strings into their constituent words requires $O(m+n)$ time, and determining the length of the longest common prefix and suffix requires $O(min(m, n))$ time to complete. The space complexity is $O(m+n)$, as the list of words are kept in memory until the algorithm exits.  
  
