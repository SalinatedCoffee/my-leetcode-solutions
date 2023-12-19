## 647. (M) Palindromic Substrings

### `solution.py`
The intuitive solution is to try and find the longest palindromic substrings at every possible center in `s`. We define a function `count` that takes 2 integers representing the proposed center to start the search from. The reason that this is represented by 2 integers instead of 1 is to account for the case where the palindrome has an even length. For palindromes that are centered at the `i`th character, we would call `count(i, i)`. For palindromes that are centered at the interstice between the `i`th and `i+1`th characters, we would call `count(i, i+1)`. `count` simply expands outwards incrementally, until a mismatching pair of characters is found. Every time a matching pair is found, it also means that a new palindromic substring has been discovered, and a global counter `self.ret` is incremented by `1`.  
When all possible centers have been considered we simply return the value `self.ret`, as it will contain the total number of palindromic substrings in `s`.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is the length of `s`. There are $2n-1$ possible centers in string `s`. For each center we expand outwards in an attempt to find the longest palindrome about that center, the length of which is bound by $n$. Therefore, this search will take $O(n)$ time to complete - hence the overall time complexity of $O(n^2)$. The space complexity is $O(1)$.  
A linear time solution exists for this problem, which is known as [Manacher's algorithm](https://cp-algorithms.com/string/manacher.html). This algorithm takes a dynamic programming approach and exploits the properties of palindromes to achieve its linear time complexity. Simply put, it makes clever use of the properties of palindromes nested within another palindrome to use previously computed results in the computation of new ones. The linked article (as well as Manacher's original paper published in 1975) is an interesting read. Revisiting this problem using this approach would be a good follow-up exercise.  
  

