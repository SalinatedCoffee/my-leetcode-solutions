## 592. (M) Fraction Addition and Subtraction

### `solution.py`
`expression` is a string consisting of only the characters `0` to `9`, `-`, `+`, and `/`s, which represents a mathematical expression. All of the terms are expressed as valid irreducible fractions having a denominator within the range `[1, 10]`. The `+` character is implied when the first term is positive. A few examples of `expression` would be `-1/2+3/4`, `1/2-3/5-44/3`, or `0/5+0/10`. We are asked to evaluate the value of `expression`, and return it as an irreducible fraction in string form. If `expression` evaluates to `0`, we should return `0/1`.  
The first order of business would be to parse `expression` into substrings that we can easily work with. Thankfully, this can be relatively easily achieved using Python's built in regular expression module. After splitting `expression` into its terms, we compute the sum of the numerators of each denominator. Once this is complete, we filter out the denominators where the sum of numerators are `0`. The least common multiple of the remaining denominators are then computed, after which the sum of all non-zero numerators can be computed. At this point we will have the numerator and denominator of the final value, which we reduce by using Python's built in GCM function.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `expression`. Parsing `expression` using a regular expression takes $O(n)$ time to complete. The following LCM and summation steps each takes $O(1)$ time since there are a fixed number of denominators in `expression`(assuming that `math.gcd()` takes $O(1)$ time to complete). The space complexity is also $O(n)$ since the list of the parsed terms of `expression` is kept in memory.  
  

