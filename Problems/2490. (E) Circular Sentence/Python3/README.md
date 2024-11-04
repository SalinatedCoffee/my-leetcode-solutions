## 2490. (E) Circular Sentence

### `solution.py`
A sentence is a string that contains lower/upppercase English letters and whitespaces, without any leading or trailing whitespaces. This means that a sentence can be broken down into words by splitting it into substrings using whitespaces as the delimiter. A sentence is 'circular' when it satisfies these two conditions:  

- The first character of the first word and the last character of the last word are the same
- The last character of a word is identical to the first character of the next word

According to these rules, the sentence `The quick brown fox jumps over the lazy dog` would be an example of a non-circular sentence. An example of a circular sentence would be `The energetic cat trots slowly yet`. We can largely think of this problem as having 2 steps; splitting the given sentence `sentence` into its constituent words, and then verifying whether the sentence is circular by checking each word in the sentence. The first step can be easily achieved by using Python's built in `string.split()` method that uses whitespaces as the delimiter as default. The second step can also trivially be solved by simply iterating over the list of words generated in the previous step. Because Python allows negative indices(which counts from the right instead of the left), we can compare words at index `i` and `i-1` without having to handle the edge case of `0`. If the appropriate pair of characters does not match at any point during the iteration, we can immediately return `False`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `sentence`. Splitting `sentence` by whitespaces requires $O(n)$ time to complete. As the number of words in `sentence` is bound by $n$, the time required to iterate over the list of split words is also $O(n)$, bringing the overall time complexity to $O(n)$. The space complexity is $O(n)$, as the list of split words is kept in memory until the algorithm exits.  
  

