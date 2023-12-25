## 1758. (E) Minimum Changes To Make Alternating Binary String

### `solution.py`
At first glance this may seem like a dynamic programming problem, but upon further inspection we can see that it is actually much more simpler. An alternating binary string can only exist as one of two cases; it can begin with a `0`, or it can begin with a `1`. For the former, every odd character must be `0` and every even character must be `1`, and vice versa for the latter. Thus, if we count the number of `1`s (or `0`s) in the even and odd positions, we can determine the case that would require the least operations. The number of even positions in `s` is `len(s) // 2`, and the number of odd positions is `len(s) // 2 + len(s) % 2`. If `even` and `odd` are the number of `1`s in the even and odd positions respectively, we can compute the number of operations required to change `s` into an alternating string. If we want to change `s` into an alternating string that starts with a `0`, we need to change all `1`s in the odd positions to `0` and all `0`s in the even positions into `1`. We already know the number of `1`s in the odd positions, and the number of `0`s in the even positions is simply `len(s) // 2 - even`. Thus, the number of operations required is `len(s) // 2 - even + odd`. We can use the same logic to determine the number of operations required to change `s` into a string that starts with a `1`, and return the smaller value amongst the two.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the length of `s`. `s` is iterated over once, and each character takes constant time to process. The space complexity is $O(1)$.  
  


### `solution_2.py`
If we think about the first approach a bit more, we can see that every change that we would have to make to convert `s` into one of the alternating strings would not need changing for the *other* case. For example, if `s = "110010111"` and we wanted to change it to the alternating string that begins with a `1`(`101010101`), we would have to perform 3 operations: flip the second and fifth `1` to `0`, and the first `0` to `1`. If we wanted to change to the other string (`010101010`), we would have to make 6 operations: change the first, second, third and fifth `1` to `0`, and the second and third `0` to `1`. The key here is noticing that the complement of a set of operations is that required to change `s` to the *other* alternating string. That is, if 3 operations are required to convert `s` into the alternating string beginning with a `1`, we would need `len(s) - 3` operations to convert `s` into the string starting with a `0`. Thus, we only need to count the number of operations for one string since we can use that to compute the number of operations for the other string.  
Instead of keeping track of even and odd positions separately, we simply keep track of one integer `one`, which represents the number of operations required to convert `s` into an alternating string starting with `1`. Every time a character at an odd position is `0` or that at an even position is `1`, we increment `one` by `1`. Once all characters of `s` have been examined, the number of operations required to convert `s` into an alternating string that starts with `0` is simply `len(s) - one`. We return the smaller value of the two.  

#### Conclusion
The time and space complexity for this problem is identical to that of the previous solution.  
  

