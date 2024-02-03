## 150. (M) Evaluate Reverse Polish Notation

### `solution.py`
We are asked to evaluate an expression written in the [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation). In RPN, the operands are written first, after which the operator is written. So for example, the expression $1 - 2$ would be written as $1\ 2\ -$ in RPN. If we abstract the values away and replace them with expressions, we can see that an expression written in RPN can easily be evaluated using a stack.  
An empty stack is first initialized before iterating over the list of tokens. During the iteration, if the current token is an operand (is a numeric value) we simply push it onto the stack. Otherwise, we pop 2 items off of the stack and compute the value between them using the current token as the operator. Since it is guaranteed that `tokens` is a valid expression in RPN, and that there are no divisions by zero, we do not have to add additional guards.  
Once all tokens have been considered we can simply return the single element left in the stack.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `tokens`. `tokens` is iterated over exactly once, and processing a single token takes $O(1)$ time (assuming that `int()` takes $O(1)$ time as well). The space complexity is also $O(n)$ as `vals` can at most contain roughly $n / 2$ values.  
  

