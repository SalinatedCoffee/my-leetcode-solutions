## 2273. (E) Find Resultant Array After Removing Anagrams

### `solution.py`
`words` is a list of strings, with each string consisting of only lowercase English letters. Within a single operation, we can select any index `i` where `0 < i < len(words)`, and remove `words[i]` from the list if `words[i-1]` is an anagram of `words[i]`(and vice versa).  
We know that two strings are anagrams of each other if the number of occurrences of each unique letter exactly match. For example, `dog` and `god` are anagrams of each other since they both contain the letter `d`, `o`, and `g` exactly once. Hence, we can verify whether two strings are anagrams of each other by generating their respective frequency list of unique characters and comparing them. This can be trivially implemented in Python by using `Counter`s, which by default counts the occurrences of each unique character when given a string.  
Moving on to the removal operation, our first instinct is to store remaining elements in a stack. However, since we only remove one of the two matching strings, we may simply store elements in a list. Iterating over `words` from left to right, we look at the last element of the list of remaining words. If that element is an anagram of the current word in `words`, we move on to the next word without doing anything. Otherwise, we append the current word to the list of remaining words before proceeding. Once all words have been examined, we can return the list of remaining words.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $n$ is the length of `words` and $m$ the average length of the strings in `words`. Each string in `words` is iterated over exactly once in order to generate its frequency list. Since the runtime of this operation scales linearly with the length of the string, we can say that this operation will take $O(m)$ time for a string in `words`. As `words` contains $n$ such strings, the overall time complexity comes out to be $O(mn)$. The space complexity is $O(n)$, as we store the remaining words in a separate list.  
  

