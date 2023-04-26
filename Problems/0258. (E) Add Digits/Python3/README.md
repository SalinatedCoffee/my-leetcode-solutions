## 258. (E) Add Digits

### `solution.py`
Using simple iteration, this is an easily solvable problem. We simply compute the sum of the digits through modulo operations and take the sum of the previously computed sum if it is larger than 10.  

#### Conclusion
This solution runs in $O(\log n)$ time where $n$ is `num`. Every time a digit sum is computed, the number gets reduced by at least one order of magnitude, hence the logarithmic running time. The space complexity is $O(1)$.  
  

### `solution_2.py`
The follow-up question requires us to apply a mathematics-based approach in order to achieve constant time complexity. This exact problem is also known as computing the [digital root](https://en.wikipedia.org/wiki/Digital_root), which has several closed-form formulas that are computable in constant time. The one used here is  
$$
dr_b(n) =
	\begin{cases}
		0 & \quad \text{if } n = 0,\\
		1 + ((n-1) \mod (b-1)) & \quad \text{if } n \neq 0.
	\end{cases}
$$  
Where $dr_b(n)$ is the digital root of $n$, and $b$ is the base of $n$ (so in this case, $b = 10$). This formula can be written as a single ternary if-else statement where its evaluated value can be returned directly.  

#### Conclusion
The time and space complexity of this solution is $O(1)$.  
  

