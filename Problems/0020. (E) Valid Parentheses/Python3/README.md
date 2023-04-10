## 20. (E) Valid Parentheses

### `solution.py`
The rule is that whenever a close parentheses is encountered, it must match the *most recent* unmatched open parentheses. This is trivial to keep track of, when all open parentheses are stored in a stack. Whenever a close parentheses is encountered, we pop an element off of the top of the stack and compare it against the character of question. We may return early whenever a mismatch is found, as that invalidates the entire set of parentheses.  
One thing to remember is that we still need to check whether the stack is empty after we have finished iterating over `s`. If it is indeed empty, then `s` is a valid set of parentheses.  

#### Conclusion
This solution runs in $O(n)$ time where $n$ is the length of `s`. The space complexity is also $O(n)$, as in the worse case all characters in `s` will be stored in `stack`.  
  

