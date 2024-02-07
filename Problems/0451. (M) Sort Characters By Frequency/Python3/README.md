## 451. (M) Sort Characters By Frequency

### `solution.py`
We simply need to count the number of occurences of each unique character in `s`, and construct a string using the unique characters in descending order of their frequencies. Because `s` can contain lower and uppercase English letters, as well as digits, we need to use a dictionary to keep track of the frequency count of each unique character. The characters are counted using a `Counter`, after which it is converted into a list. Then, we sort the list in descending order of the frequencies. The sorted list can now be iterated over while incrementally constructing the string to be returned.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. Initializing the `Counter` takes $O(n)$ time, as we have passed `s` as the argument. The key-value pairs of `Counter` is then sorted in descending order of the frequencies. However since `Counter` can hold at most 62 key-value pairs (lower/upper case letters + digits) we can consider this step as taking constant time to compute. The space complexity is $O(1)$, due to the same reason why `Counter` takes $O(1)$ time to sort.  
  

