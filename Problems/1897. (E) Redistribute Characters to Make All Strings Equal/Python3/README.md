## 1897. (E) Redistribute Characters to Make All Strings Equal

### `solution.py`
As we can redistribute letters among the words without any restrictions, the only thing that becomes relevant is the number of each character across `words`. If all unique characters have a count that is divisible by the number of words in `words`, it means that we can redistribute the characters to make all words equal.  
We use the list `freq` to count the number of occurrences of each unique letter. Because we know that every word in `words` contains only lowercase English letters, we can use a list instead of a dictionary. For each word we examine its characters, and increment the corresponding value in `freq` by `1` for every occurrence. Once all words have been examined we check the contents of `freq` and return `False` as soon as a value is determined to be indivisible by `len(words)`. If all values pass the check, we return `True`.  

#### Conclusion
This solution has a time complexity of $O(nk)$, where $n$ is the length of `words` and $k$ is the average length of a word in `words`. Each character of every word in `words` is counted, hence the overall time complexity is $O(nk)$. The space complexity is $O(1)$.  
  

