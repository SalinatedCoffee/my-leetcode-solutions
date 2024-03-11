## 791. (M) Custom Sort String

### `solution.py`
We are asked to sort `s` according to the order described by `order`. Essentially, we are grouping the characters in `s` and ordering them in the order of characters in `order`. Do achieve this we first need to count the frequency of each unique characters in `s`, which can be done by instantiating a `Counter` while providing `s` as the argument. Then we iterate over `order`, appending each 'section' of the sorted string if a character in `order` exists in `s`. Finally, we simply add all remaining characters to the end of the constructed string as any permutation is valid as long as the string respects the ordering of characters as defined in `order`.  

#### Conclusion
This solution has a time complexity of $O(m+n)$ where $m$ and $n$ are the lengths of `order` and `s`, respectively. Initializing the `Counter` takes $O(n)$ time to complete. Constructing the sorted string takes $O(n)$ time, since appending a string is a linear time operation that scales to the length of the string being added(this optimization is however, implementation specific; it is the [default behavior for CPython](https://stackoverflow.com/questions/37133547/time-complexity-of-string-concatenation-in-python), which is most widely used). Hence, the overall time complexity becomes $O(m+n)$. The space complexity is $O(n)$.  
  

