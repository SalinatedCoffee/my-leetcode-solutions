## 139. (M) Word Break

### `solution.py`
We first need to understand that a brute force approach will not work for this problem. The problem can be thought of recursively, where the string is split and if the first half is a valid word we recurse on the second half. Given a string of length $n$ then, there are $n$ positions where a split can happen. At each position, we can either split or not split the string - so overall, there are $2^n$ possible ways of splitting a string of $n$ length.  
This is obviously not a feasible algorithm to run, and we certainly can do better. Returning to the recursive portion of the brute force solution, we can keep track of whether the prefix of a substring is splittable or not. We store these values in the list `dp` that has a length of `len(s)+1`. The value of `dp[i]` refers to whether the substring `s[0:i]` is splittable or not. An empty string is considered to be splittable and thus we set `dp[0]` to `True`.  
To check whether a substring is in the dictionary or not, we can implement a simple Trie. Before iterating over `s`, we first insert all words into the trie and call `find()` to look up a word in the dictionary.  
Finally we need to check all possible substrings of `s`, so we use a nested loop and update `dp[i]` where `i` is the outer loop's loop variable (index of last character in the current word).  
  
#### Conclusion
The solution takes $O(n^3+mk)$ time to run, where $n$ is the length of $s$, $m$ is the number of words in the dictionary, and $k$ is the average length of the words in the dictionary. The nested loop iterates $n^2$ times, and the trie lookup takes $n$ time in the worst case. $mk$ simply comes from the fact that every word in the dictionary is inserted into the trie and the running time of a single insertion scales with the length of the word being inserted.  
In terms of memory, the solution uses $O(26^k + n)$ space. The trie is based on lists of fixed length and thus takes up $26^k$ space (admittedly a bit hand-wavy, but should be in a good enough ballpark), and `dp` has a length of `len(s)+1`.  

### `solution_2.py`
After implementing a trie, we (somewhat embarrasingly) realize that we can use a set instead as we only need to check whether a substring is in the dictionary or not(though if the vocabulary contains a lot of the words that share similar prefixes an optimal trie implementation may use less memory). We also see that we don't need to update `dp[i]` *every* iteration, but only if the current substring is a valid word and the prefix is splittable. Lastly, if we find a prefix+substring combination that is valid there is no point in checking for other words that end in index `i`. So we can just break out if the inner loop early if we find a substring where `dp[i]` evaluates to `True`.  

#### Conclusion
This solution has a time complexity of $O(n^3 + mk)$ as the hashing of a string of size $n$ takes $O(n)$ time. The space complexity is $O(m+n)$, since `words` contains all of the words in `wordDict`.  
In practice however, this solution will run much faster than the first solution thanks to the use of hashing (faster than dereferencing pointers) and the optimizations made in how `dp` is updated.  
  