## 344. (E) Reverse String

### `solution.py`
Given a list of characters, we are asked to reverse the list in-place while using $O(1)$ extra space. This can be trivially implemented by using an index-based swap where the characters at `s[i]` and `s[len(s)-i-1]` are swapped, where `i` is in the interval `[0, len(s)//2]`.  

#### Conclusion
The time complexity for this problem is $O(n)$, where $n$ is the length of `s`. There are $O(n)$ pairs of characters in `s`, and each pair takes $O(1)$ time to swap. The space complexity is $O(1)$, as requested by the problem.  
  

