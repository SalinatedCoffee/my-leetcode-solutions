## 1957. (E) Delete Characters to Make Fancy String

### `solution.py`
Given the string `s`, we are asked to make the string a 'fancy string' and return the result. A fancy string is simply a string that does not contain 3 identical consecutive characters. For example, the string `aabbbbbc` is not a fancy string. In order to make it fancy we would have to remove 3 `b`s, resulting in the fancy string `aabbc`. Because the substring length is fixed, we can easily solve this problem through a sliding window approach.  
We first initialize the empty list `res`, which we will use to store the characters of the resulting fancy string. The first 2 characters of `s` are added to `res` before we start iterating over `s`. Starting with the 3rd character, we look back on the 2 previous characters and compare them with each other. If all 3 characters are identical, we simply skip the current character. Otherwise, we append the current(rightmost character of the window) character to `res` and advance the window by 1 before repeating the steps described. Once we reach the end of `s`, `res` will contain the characters of the fancy string, which we concatenate into a single string before returning it.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. There are $n-2$ possible windows in `s`, and evaluating each window takes $O(1)$ time to complete. Concatenating the contents of `res` takes $O(n)$ time, as the length of the fancy string is bound by $n$. Thus, the overall time complexity of this solution is $O(n)$. The space complexity is also $O(n)$, as `res` is kept in memory until the algorithm finishes running.  
  

