## 1704. (E) Determine if String Halves Are Alike

### `solution.py`
There are many ways to approach this problem, as is usually the case with those labeled easy. Here we have opted to take a two pointer approach that traverses each half of `s` simultaneously. For each character in either half we increment / decrement a counter if it is a vowel, depending on whether it is in the first or latter half. Once every character in `s` has been examined, we simply check whether the counter is `0`. If it is, than the two halves are alike. Otherwise, we return `False`.  

#### Conclusion
The time complexity of this solution is $O(vn) = O(10n) = O(n)$, where $n$ is the length of `s` and $v$ is the number of vowels. Determining whether a character is a vowel or not takes $O(v)$ time as we use Python's `in` keyword on a string of vowels, which is a linear-time operation. This is performed for every character in `s`, bringing the overall time complexity to $O(n)$. The space complexity is $O(v) = O(1)$ as we keep the vowels in memory in the form of a string.  
  

