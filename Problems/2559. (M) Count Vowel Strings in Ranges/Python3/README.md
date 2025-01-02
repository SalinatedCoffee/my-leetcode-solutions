## 2559. (M) Count Vowel Strings in Ranges

### `solution.py`
A single query on the list of strings `words` involves the integers `i` and `j`, where the result of the query being the number of elements that starts with *and* ends with a vowel in the subarray `words[i:j+1]`. Given the list of queries `queries`, we are ask to return the list of query results where the `i`th value is the result of query `queries[i]`.  
We can trivially determine whether a string is 'valid' simply by examining its first and last characters(for a string consisting of only 1 character, these characters are the same). If we were to evaluate a query using brute force, we would have to scan through the relevant portion of `words` while counting the number of valid strings. Instead, we can preprocess `words` to create a list containing the valid string counts for each and every prefix of `words`. For example, if the query range is `i` up to `j`, we would need to determine the number of valid strings in the subarray `words[i:j+1]`. If we knew the number of valid strings in `words[:i]` and `words[:j+1]` beforehand, we can determine the result of the query simply by subtracting the former from the latter. In other words, we can quickly compute the result of query `[i, j]` by computing the value of `prefix[j] - prefix[i]`, where `prefix[i]` is the number of valid strings in the subarray `words[:i]`.  

#### Conclusion
This solution has a time complexity of $O(n+m)$, where $n$ is the length of `words` and $m$ is the length of `queries`. Preprocessing `words` and populating `prefix` completes in $O(n)$ time. The list of queries is then evaluated. Because evaluating a single query is a $O(1)$ time operation, evaluating $m$ queries will require $O(m)$ time. The space complexity is $O(n)$ due to `prefix`.  
  

