## 28. (M) Find the Index of the First Occurrence in a String

### `solution.py`
A brute force approach is trivial to implement, and is accepted by the online judge. We simple iterate over `haystack` and compare `needle` starting at every character in `haystack`. If a mismatch is detected we advance to the next character in `haystack` and try matching again.  
  
#### Conclusion
The time complexity for this solution is $O(nm)$ where $n$, $m$ are the length of `haystack` and `needle`, repectively. The space complexity is $O(1)$.  
  
  
### `solution_2.py`
The [Knuth-Morris-Pratt algorithm](https://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm) is an optimized version of the brute force solution, which takes `needle` into account and jumps foward within `haystack` as much as possible. Before iterating over `haystack`, we precompute an array of length `len(needle)` containing the longest length of matching proper pre/suffixes at each index. Using this we can determine how far we can advance in `haystack` whenever a mismatch is detected, thus improving upon the brute force algorithm. Refer to the Wikipedia link or LeetCode's [editorial](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/editorial/) for details on how the precomputed array is generated in linear time.  

#### Conclusion
KMP is based on some statistical assumptions on `haystack`, and the worst case time complexity is still $O(nm)$. The space complexity is $O(m)$, as the preprocessed array has the same length as `needle`.  
If you didn't know about this algorithm beforehand, this problem would definitely be *at least* a hard problem - coming up with an algorithm like this on the spot is not a trivial thing to do, to put it lightly.  
  
  