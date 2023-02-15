## 76. (H) Minimum Window Substring

### `solution.py`
We will be employing the sliding window technique as the problem *literally has the word 'window' in its title*, and reading the description it seems that it would indeed be a viable approach to take. First we start by counting the number of characters in `t` and `s[:len(t)]`. Instead of dealing with ASCII codes which would be a pain since the alphabet contains both lowercase and uppercase letters we will simply be using a dictionary. If all unique characters in `t` exist in a substring of `s` and the counts for those letters in `s` are greater than or equal to those in `t`, that substring contains all of the letters in `t`. Matching `t` and a substring of `s` can be achieved by keeping track of two numbers; the number of unique letters in `t` and the number of matching character pairs between `t` and the substring of `s`. When a letter is added or removed, we increment `cnt_s[letter]` and compare it with `cnt_t[letter]`. For the former case we increment `matched` when they are equal. For the latter case we decrement when `cnt_t[letter]` is larger than `cnt_s[letter]`.  
Iterating over `s`, we first add the letter at `j` and check if `t` and the current window bound by `[i,j]` match. If true, we try incrementing `i` until we find the smallest window that still matches `t`.  
After exiting the loop, `res` will contain the desired substring of `s`.  

#### Conclusion
The solution has a time and space complexity of $O(m+n)$, where $n$ is the length of `s` and $m$ is the length of `t`.  
There is an optimization that can be made if `s` is mostly comprised of letters not in `t`, which is removing the offending letters from `s` and storing the original indices with the remaining ones. For example, if `s = "AAABCCCDEEE"` and `t = "BD"` `s` would look something like `[(B,3), (D,7)]`. The method described above can still be applied on the transformed `s`.  
  
