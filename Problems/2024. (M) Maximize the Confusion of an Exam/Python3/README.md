## 2024. (M) Maximize the Confusion of an Exam

### `solution.py`
We want to maximize the number of consecutive problems with the same answer key; that is, we want to maximize the length of a subarray containing either only `T`s or `F`s. This can be easily solved by taking a sliding window approach, where we iterate over `answerKey` once for each answer key. The implementation itself is textbook sliding window - we keep track of the position of the start of the window and count the number of answer keys that we want to change. Once the number exceeds that of `k`, we keep advancing the start of the window until the count drops below it.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `answerKey`. `answerKey` is iterated over twice, and for each traversal `l` will be iterated $O(n)$ times. The space complexity is $O(1)$.  
Like many other basic sliding window problems, this problem can also be solved by using prefix sums with binary search.  

