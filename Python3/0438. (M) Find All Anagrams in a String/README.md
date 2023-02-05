## 438. (M) Find All Anagrams in String

### `solution.py`
This is a near-exact copy of [problem 567](https://leetcode.com/problems/permutation-in-string), the only difference being that we are asked to return a list of indices where the permutation begins instead of the number of contained permutations. We can employ the same sliding window strategy as problem 567 where we count the number of letters in `p` and `s[i:i+len(p)]` and add `i` to the return list whenever a match is found.  

#### Conclusion
The time complexity is $O(m+26n)$ where $m$ is the length of `p` and `n` is `len(s) - len(p)`. The space complexity is $O(1)$ (scales with the size of the alphabet of `s` and `p`).  
  

### `solution_2.py`
Instead of doing an element-wise comparison for `cnt_p` and `cnt_s`, we can take a localized approach where we only examine the letters that have had their count updated. We can achive this by keeping track of how many letters have the same count in `p` and `s[i:i+len(p)]`. We will name this counter `match`. Naturally `match` being equal to `26` would indicate that 26 letters have the same count, and that both strings have same letter counts. Updating `match` is trivial; if a letter count has been incremented we check if the count in `p` is equal to the count in `s` plus 1, and vice versa.  

#### Conclusion
This solution runs in $O(m+n)$ time where $m$ is the length of `p` and $n$ is equal to `len(s) - len(p)`. Memory-wise, the solution uses $O(1)$ space.  
  
