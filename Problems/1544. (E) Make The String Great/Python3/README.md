## 1544. (E) Make The String Great

### `solution.py`
As we are asked to continuously remove characters until the string is 'good' we need to take into account cases such as `s = "abBA"`, where deleting `"bB"` would result in `"aA"`, which would also need to be deleted. If you have solved parentheses-related problems before, you may realize that this problem is very similar to that type of problems, as we essentially want to 'match' the current character with those previously discoverd based on some criteria. Here, we need to match letters while ignoring case. There are many ways to do this, but here we have chosen to use the ASCII code difference between two characters. As we iterate over `s`, we simply check whether the character at the top of the stack matches with the current character. If so, we simply pop the character from the top of the stack and discard the current one. Otherwise, we push the current character to the top of the stack. Once the entirety of `s` has been examined, the characters stored in the stack will form the 'good' string after removing characters from `s`.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `s`. `s` is iterated over exactly once, with each character requiring constant time to process. The space complexity is also $O(n)$ as the stack can contain at most $n$ characters.  
  

