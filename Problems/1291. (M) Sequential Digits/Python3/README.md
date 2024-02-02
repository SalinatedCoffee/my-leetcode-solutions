## 1291. (M) Sequential Digits

### `solution.py`
We essentially want to generate all possible sequential values and only select the ones that fall between `low` and `high`. Generating the first integer for a fixed number of digits (for example `1234` for 4 digits) is trivial. How can we 'increment' this value to the next valid sequential number? This is also easily achievable by adding `1` to each digit. So if a sequential number `i` is 4 digits long, we can trivially compute the next sequential number by computing `i + 1111`. Whenever the rightmost digit becomes `0` we know that we have overstepped our bounds as the digit would have previously been `9`. We now can generate a list of all sequential values for a specific number of digits. As we want all sequential numbers between `low` and `high`, we can sequentially generate the lists of sequential numbers by starting at the number of digits of `low`. If at any point a value is larger than `high`, we return immediately as any values generated after that point would also be larger than `high`.  

#### Conclusion
This solution has a time complexity of $O(n^2)$ where $n$ is the number of digits of `high`. Generating the initial sequential value with $i$ digits takes $O(i)$ time. We do this for every digit count starting with that of `low` up to `high`; hence the overall time complexity of $O(n^2)$. The space complexity is $O(1)$, excluding the return list `ret`.  
  

