## 1071. (E) Greatest Common Divisor of Strings

### `solution.py`
If the strings can be divided by a common substring, we can reason that the substring must also be a *prefix* of both strings. Building upon this intuition we can use a brute force approach where we try all possible common prefixes. Starting from the beginning of both strings, we check if the characters at the same index are the same. If yes, we simply take the prefix (of range `[0, i]`) and match it against both strings.  
One optimization we can add is to skip the prefix when at least one of the strings has a length that is not divisible by the length of the prefix.  
  
#### Conclusion
The solution takes $O(\text{min}(m,n)*(m+n))$ time where $m,n$ are the lengths of `str1` and `str2`. $\text{min}(m,n)$ comes from the fact that we iterate up to the value of `min(len(str1), len(str2))`, and $m+n$ from the matching of `prefix` to both strings.  
In terms of space complexity the algorithm uses $O(\text{min}(m,n))$ space since `prefix` at most has the same length as the shorter string of `str1` and `str2`.  
  

### `solution_2.py`
The brute force solution works well with the given constraints, but we can take a different approach by further examining the relationship between the GCD substring and the 2 original strings.  
We can first start with the mathematical GCD of both strings. The GCD of the string lengths can be easily computed with `math.gcd()` (or trivially implemented using the [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) for languages without a built-in equivalent). The question, then, is if a GCD substring exists, is the length always equal to the GCD we computed earlier? Let's assume that a GCD substring exists, and the length is smaller than the GCD of `len(str1)` and `len(str2)`. Since both strings are divisible by the GCD substring it must be the case that the length of the GCD substring is a common factor of the length of the input strings. But from the [properties of the GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor#Properties) we know that *the GCD is always divisible by any of the common factors*. So we can construct a substring of length GCD that is divisible by the GCD string. However, the new substring must also divide the input strings since it has a length of GCD and is comprised of the GCD substring which by definition also divides the two strings - so the assumption that there exists a GCD substring that is shorter than the GCD of the input strings must be false.  
Now that we have established that if a common divisible substring exists its length will always be equal to `math.gcd(len(str1), len(str2))`, we need to figure out a way to trivially check whether two strings have a common divisor or not. When we substitute a common substring with a single letter we can see that the input strings just become consecutive runs of that single letter (eg. `ABCABCABC` and `ABCABC` become `VVV` and `VV` respectively when `V == ABC`). Thus, the concatenation of the input strings will always be the same regardless of order - which is trivial to verify.  

#### Conclusion
The time and space complexity of this solution is $O(m+n)$ since we compare two strings of length $m+n$ (`math.gcd()` takes $O(\log(\min(m,n)))$ time so $m+n$ is the dominant factor in terms of time).  
This is a weird one - I agree that coming up with the first solution is easy as the label suggests, but the second solution feels more like a difficult medium.  
  
