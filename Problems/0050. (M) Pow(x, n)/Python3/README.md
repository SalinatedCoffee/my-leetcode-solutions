## 50. (M) Pow(x, n)

### `solution.py`
Since we are working with Python, we thankfully do not have to worry about over/underflow. The naïve solution is trivial, as we only need to multiply `x` (or its reciprocal) with itself `n` times. However as the bound on `n` is very large this approach will take too long. We can dramatically cut down on the number of multiplication steps through a little bit of (admittedly not that intuitive) math. Let `x = 3` and `n = 100`. We eventually want to compute the value $3^{100}$. Through the power rule, we can rewrite this as $(3^2)^{50}$. If we apply this again we get $((3^2)^2)^{25}$. This time the outer exponent is odd, but this can be trivially solved by 'pulling out' a single $3$, which will reduce the exponent by $1$. So $(((3^2)^2)\cdot 3)^{24}$, at which point we can apply the same rule yet again. Notice that each time the rule is applied the outer exponent is reduced by half, therefore the number of multiplications across the entire computations gets reduced logarithmically. This technique of computing exponentials is called binary exponentiation, due to the method reducing the exponent with repeated squarings of the base.  

#### Conclusion
This solution has a time complexity of $O(\log n)$ where $n$ is `n`. The space complexity is $O(1)$.  
  

