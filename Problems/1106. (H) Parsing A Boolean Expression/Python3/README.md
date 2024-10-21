## 1106. (H) Parsing A Boolean Expression

### `solution.py`
A boolean expression follows the grammar described below:

- `!(A)`: Negate(logical NOT) the evaluated value of `A`.  
- `|(A)`: Logical OR all terms of `A`.  
- `&(A)`: Logical AND all terms of `A`.  
- `t`: Evaluates to `True`.  
- `f`: Evaluated to `False`.  
- `,`: Separates terms.  

One example of a valid expression that follows this grammar would be `!(&(|(t,f,t),&(t,f)))`. Stepping through the expression, the innermost `|()` evaluates to `True`(`True | False | True`), and the innermost `&()` evaluates to `False`(`True & False`). The expression now becomes `!(&(t,f))`, and because the inner `&()` evaluates to `False`(`True & False`), the entire expression evaluates to `True`. Given these rules and the string `expression` containing a **valid** boolean expression, we are asked to evaluate the expression and return its value. Because the grammar is simple and `expression` is guaranteed to contain a valid expression, we can (relatively) easily parse the expression iteratively by using a pair of stacks. One stack will contain the terms of the expression, and the other stack will contain the operations. When a close parentheses is encountered, the terms in the current 'scope' are evaluated by looking at the top of the operation stack. The evaluated value is then pushed back onto the stack, and the operation is popped off of the operation stack. Once the end of `expression` is reached, the stack will contain only one element, which is the desired value.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `expression`. `expression` is iterated over once, and processing each character takes $O(1)$ time as pushing/popping items off of a stack are all constant time operations. The space complexity is also $O(n)$, due to the stacks `stack` and `opstack`.  
  

