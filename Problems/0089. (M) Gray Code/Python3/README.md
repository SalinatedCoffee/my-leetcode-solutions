## 89. (M) Gray Code

### `solution.py`
This one of *those* problems where solving it is trivial if you know the algorithm beforehand, but actually coming up with said algorithm in an interview setting would be near impossible for the average person.  
With that being said, the algorithm to generate a list of Gray codes for `n` bits is neatly described on [Wikipedia](https://en.wikipedia.org/wiki/Gray_code#Constructing_an_n-bit_Gray_code). In essence, it recursively generates the list by reusing the list from the previous step. Generating `n` bit Gray codes depends on the codes for `n-1` bits, `n-1` bits depend on `n-2` bits, and so on. Given the list of Gray codes for `n` bits, we first create a reversed copy of this list. We then prepend the single bit `1` to all values in the reversed list, after which we simply contatenate the original list and the reversed, prepended list together to get the Gray codes for `n+1` bits. The base case here would be when `n == 1`, in which case the list would simply be `[0, 1]`.  

#### Conclusion
The time complexity of this solution is $O(n2^n)$ where $n$ is `n`. `grayCode` is called $n$ times, and each call takes $O(2^n)$ time as it involves copying and reversing the list of Gray codes from the next recursive call. The space complexity is $O(2^n)$. Even when excluding the final list that is returned, the intermediate lists will use $O(2^n)$ memory.  
  

