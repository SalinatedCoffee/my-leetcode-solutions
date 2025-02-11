## 3174. (E) Clear Digits

### `solution.py`
A digit can be removed from a string by removing the first digit and the letter closest to that digit on its left. Given the string `s`, comprised of lowercase English letters and numbers, we are asked to return the resulting string after removing all digits. Upon reading the problem description we can immediately see that the problem can be trivially solved by using a stack. Iterating over `s` from left towards the right, we push the current character on the stack if it is a letter, or pop an item off of the stack if it is a number. Once all characters have been examined, we simply concatenate the elements on the stack to a string in the appropriate order.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. All characters of `s` are examined, and since interactions with the stack take $O(1)$ time to complete, the overall time complexity is $O(n)$. The space complexity is also $O(n)$, due to the list `stack`.  
  

