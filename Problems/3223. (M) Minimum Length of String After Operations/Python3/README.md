## 3223. (M) Minimum Length of String After Operations

### `solution.py`
Any number of operations can be performed on the string `s`. In a single operation, we can:  

- Select any index `i` where `0 < i < len(s) - 1` and there exists at least 1 character to the left *and* right of `s[i]` that are identical to `s[i]`.  
- Select the closest character to the left of index `i` that is equal to `s[i]`, and delete it.  
- Select the closest character to the right of index `i` that is equal to `s[i]`, and delete it.  

Given these instructions, we are asked to return the minimum length of `s` after performing any number of operations.  
Summarizing, we can select any character `s[i]` and remove the 2 characters equal to `s[i]` that are closest to the selected character on either side of it. If we think about this further, we can see that selecting the closest character doesn't matter since our goal is to remove as many characters as possible. Because we can remove 2 characters in a single operation, there are 2 possible scenarios regarding a unique character in `s`. If `s[i]` appears an even number of times in `s`, removing instances of `s[i]` will eventually reduce the frequency of `s[i]` to `2`. At this point, these characters cannot be removed since we need at least 3 instances of `s[i]` when performing an operation. On the other hand, if `s[i]` appears an odd number of times in `s`, the frequency of `s[i]` will eventually become `3`. Unlike the other case, an operation *can* be performed in this state, reducing the frequency to `1`.  
We now know that if `freq[s[i]]` is the frequency of `s[i]` in `s`, all but `1` instance of `s[i]` can be deleted if `freq[s[i]]` is odd, or `2` instances if `freq[s[i]]` is even. Thus, if we generate a frequency list of unique characters in `s`, we can determine the length of the final string by simply iterating over the frequency values. If the value is odd, we add `1` to the final length. If it is even, we add `2`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. Generating the frequency list of unique characters requires iterating over the entirety of `s`, which requires $O(n)$ time to complete. Determining the length of the final string is a $O(1)$ time operation since the size of the alphabet of `s` is fixed, bringing the overall time complexity to $O(n)$. The space complexity is $O(1)$.  
  

