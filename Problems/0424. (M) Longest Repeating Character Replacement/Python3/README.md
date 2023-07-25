## 424. (M) Longest Repeating Character Replacement

### `solution.py`
If we fix the target to a single character, the problem becomes a simple sliding window problem that takes $O(n)$ time to run. Since the alphabet of `s` is rather small, we can take a brute-force approach and compute the longest replacement substring for each and every character.  

#### Conclusion
This solution takes $O(mn)$ time to run, where $m$ is the number of characters in the alphabet of `s`, and $n$ is the length of `s`. The space complexity is $O(1)$.  
  

### `solution_2.py`
For the first solution, we had to compute the length of the longest substring for each and every character. This is because we were counting the number of characters that we would have to replace to make the substring valid. If we instead we count the number of the 'target' character in a substring, we can extrapolate the number of replacements we need to make by substracting the 'target' character count from the size of the window. For example if `s = "AABBCAAAA"`, and the window is the entirety of `s`, there are 6 `A`s in `s`, and so we would need to replace `len(s)-6 = 9-6 = 3` characters to make `s` valid. If we keep this count for all possible characters then, and keep track of the largest value among these counts, we can quickly verify whether the current window is valid or not. Based on this we want to extend the window only when the largest frequency count (`max_freq`) is updated, since for two valid windows with the same size, the one with the larger frequency count can be extended further since it would have more replacement allowances than the other window. Again, as an example, given two windows `l1 = "AAABB"` and `l2 = "ABBBB"` where `k = 5` clearly `l2` can be extended further than `l1` since only 1 replacement is required for it to be valid against `l1`'s 3 replacements.  
We only shrink the window when the current one becomes invalid, which we can trivially check as mentioned earlier. When we do shrink the window, we only need to shrink it by 1 since we are only interested in the largest window in `s`, and we know that the shorter window size is valid.  
To summarize, we keep count of all characters in the current window in `freq`, and the largest count across all characters in `max_freq`. Iterating through `s` with index `i` we increment the corresponding counter of the character `s[i]`, and update `max_freq` accordingly. If the current window is invalid, we shrink the current window by 1 by advancing the left index `l` by `1` and updating `freq` accordingly. We then update `ret` with the current window size, which we simply return once the iteration has finished(notice the lack of `max()`, as the window size never decreases between updates to `ret`).  

#### Conclusion
The time complexity of this solution is $O(n)$, since we iterate over `s` once, and during each iteration we only perform a fixed number of operations that in total takes $O(1)$ time. The space complexity is $O(m)$ since the dictionary `freq` can at most contain $m$ key-value pairs.  
  

