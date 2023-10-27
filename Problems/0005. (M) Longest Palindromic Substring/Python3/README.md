## 5. (M) Longest Palindromic Substring

### `solution.py`
Being one of the classic dynamic programming problems, the recurrence relation is relatively straightforward to understand. If we were to take a brute-force approach by checking all possible substrings of `s`, the solution would have a time complexity of $O(n^3)$. We can reduce this down to $O(n^2)$ by applying dynamic programming. If we have some substring `s[i:j]` and already know that it is palindromic, we can trivially check whether `s[i-1:j+1]` is palindromic by comparing the characters `s[i-1]` and `s[j]`. If they are equal, we continue fanning outwards. If they are not, we exit immediately.  
We run the algorithm described above on all possible starting positions in `s` - that is, all pairs of `i` and `j` where `i == j` or `i + 1 == j`. Among all of the returned substrings, we simply return the longest substring.  

#### Conclusion
This solution has a time and space complexity of $O(n^2)$, where $n$ is the length of the string `s`. Each recursive state is represented by 2 integers, both of which are in the interval $[0, n)$. Computing the value of a single state takes constant time, and thus the overall time complexity comes out to be $O(n^2)$. The space complexity is also $O(n^2)$ because we store the result of each state in memory.  
For those interested there is a *linear-time* solution to the problem known as [Manacher's algorithm](https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm), which may or may not be worth looking into.  

