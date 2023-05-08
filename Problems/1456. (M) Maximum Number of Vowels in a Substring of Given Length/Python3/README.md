## 1456. (M) Maximum Number of Vowels in a Substring of Given Length

### `solution.py`
The length of the substrings we need to consider is given as the parameter `k`, which is also fixed. This greatly simplifies the problem as generating all substrings of a fixed length is trivial. Here we will take the sliding window approach where we iterate across `s` sequentially while considering the `k` sized window at the current iteration. We first need to count the number of vowels for the window `s[:k]`, which we can achieve with a `for` loop. Now we simply need to iterate over `s` with the range `[k:len(s)]`, while updating the number of vowels in the current window. If the letter that has just left the window is a vowel, we decrement the counter. If the letter that is joining the window is a vowel, we increment the counter.  
Once the loop has exited we need only return the largest value that was encountered.  
  
#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of the string `s`. `s` is iterated over once, and each iteration takes constant time to run. The space complexity is $O(1)$.  
  

