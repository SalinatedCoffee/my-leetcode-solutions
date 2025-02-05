## 1790. (E) Check if One String Swap Can Make Strings Equal

### `solution.py`
Given two strings of equal length `s1` and `s2`, we can select a character from each string and swap them. Our task is to determine whether `s1` and `s2` can be made equal by performing the swap operation **at most once**.  
First off, it is not that difficult to see that the frequencies of the unique characters in each string must match for the strings to be potentially made equal. We also realize that there can be at most 2 mismatching character pairs if the strings can be made equal, with a pair consisting of characters from each string with the same index. Thus, we can determine whether the strings can be made equal by comparing their frequency maps and counting the number of mismatching character pairs. If the maps are identical and there exists at most 2 mismatching character pairs, `s1` and `s2` can be made equal by performing the described operation.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s1`(and of course, `s2`). Generating the frequency map and counting the number of mismatching pairs are both $O(n)$ time operations. Since size of the alphabet for both strings is fixed(lowercase English letters), comparing the frequency maps will take $O(26) = O(1)$ time, bringing the overall time complexity to $O(n)$. The space complexity is $O(1)$, as the 2 frequency maps can each contain at most $26$ key-value pairs.  
  

