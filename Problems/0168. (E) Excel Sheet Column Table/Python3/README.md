## 168. (E) Excel Sheet Column Table

### `solution.py`
We can think of this problem in terms of converting an integer to a string. A solution for these types of problems usually involve extracting the least significant digit by taking the modulo and 'shifting' the number one digit towards the right through integer division. For this problem, we are essentially converting a base 26 integer to a string. However, we cannot naïvely implement the algorithm that was just described since column labels behave slightly differently than normal integers - specifically, how carries are handled. As an example, let's examine the column number `26`. Thinking about this number in terms of base 26 we can compare this value to `10` in base 10, for obvious reasons. The problem here is that `10` is base 10 has 2 digits, while `26` in base 'excel sheet' only has 1. We can mitigate this problem by checking whether the remainder (after applying `% 26`) is `0` **and** the quotient (after applying `// 26`) is non-zero. If both evaluates to `True`, it means that the current base 'excel sheet' digit is `26` and we should convert it to a `Z`. In this case we also need to remember to subtract `1` from the quotient before carrying it over, as we have already converted that digit to `Z`.  
  

#### Conclusion
This solution has a time complexity of $O(\log_{26} n) = O(\log n)$ where $n$ is `columnNumber`. The space complexity is $O(1)$, excluding the return string `ret`.  
  

