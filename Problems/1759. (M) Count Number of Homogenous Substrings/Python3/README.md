## 1759. (M) Count Number of Homogenous Substrings

### `solution.py`
We simply need to 'split' `s` into its homogenous substrings, compute the number of occurances of possible such substrings for each split, and return the summation of those values. Retrieving the homogenous substrings of `s` is trivial - here, we have opted to simply iterate over `s` while comparing against the preceding character(a sliding window approach would also work here). For a substring comprised of only 1 letter, we can easily compute the number of homogenous substrings contained within it by using the [triangular number formula](https://en.wikipedia.org/wiki/Triangular_number#Formula). We add this to the sum, take the modulo of the new sum, and repeat until we reach the end of `s`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of string `s`. `s` is iterated over once, and during each iteration we only perform a handful of constant time operations. The space complexity is $O(1)$.  
  

