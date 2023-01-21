## 491. (M) Non-decreasing Subsequences

### `solution.py`
Working with subsequences (compared to substrings) are slightly more trickier since we have to account for the fact that elements may or not be included and may not be adjacent in the original list. We'll first think of a more general situation before narrowing it down to fit the problem at hand. To enumerate all possible subsequences for example, we can quickly see that we can either include or not include an element in a subsequence. In order to apply this algorithm to this problem we only need to add another condition to check before adding an element to a subsequence, which is whether if the element is larger than or equal to the last element in the subsequence. In the actual implementation we also use a Python `set` to check if a subsequence is unique.  

#### Conclusion
This solution takes $O(2^n)$ time to run, since it tries 2 possible actions for every item in the given list. The space complexity is also $O(2^n)$ since it stores one instance of every valid subsequence.  
  

### `solution_2.py`
The time complexity of the previous solution is already optimal (since there are $2^n$ subsequences of any given list) but we can improve the space complexity by eliminating the set of seen subsequences. To achieve this we first need to identify when and how duplicate subsequences are generated. Since the subsequences are non-decreasing, duplicates such as `[1, 2, 3]` in `[1, 2, 3, 1, 2, 3]` are not possible. However when elements in a subsequence are the same (which are still *non-decreasing*) such as `[1, 1, 1, 1]`, we can see that duplicates start to appear. The problem here is that whenever we choose to exclude a certain element from the subsequence another element of the same value can take its place - in this example choosing elements `0` and `1` generates the same subsequence as excluding `0` and including `1` and `2`. The case where we choose to include an element does not matter since `[1, 1]` and `[1, 1, 1]` are different subsequences even though they are comprised by elements of the same value. Thus, we can avoid generating duplicates by checking whether the current element's value is equal to the last element in the constructed subsequence before choosing to exclude the current element.  

#### Conclusion
The time complexity is the same as the first solution, but uses $O(1)$ space by removing the need to keep a set of previously seen subsequences in memory.  
  

