## 1002. (E) Find Common Characters

### `solution.py`
As we are asked to find all common letters *including* duplicates, we cannot simply throw each word into a set and return the intersection between them. We should instead use a dictionary(or list) to generate a frequency list of each unique character in a word and manually compute the intersection between two lists. Incorporating a new frequency list into the intersection is simple; we iterate over the keys of the dictionary containing the intersection and keep the smaller value between the one in the intersection and the new word's frequency dictionaries. Once all words have been examined, we can construct the list of common characters by looking at the key-value pairs of the intersection dictionary.  

#### Conclusion
This solution has a time complexity of $O(nk)$, where $n$ is the length of `words` and $k$ is the average length of the words in `words`. All words are examined, and since producing a frequency list of a word of length $k$ takes $k$ time, the overall time complexity comes out to be $O(nk)$. The space complexity is $O(1)$ excluding the returned list of characters. While the intersection of the character frequency counts of each word is stored in a dictionary, the elements of `words` are only comprised of lowercase English letters, of which there are a fixed number of(26). Hence, the memory used by the dictionary will be $O(1)$.  
  

