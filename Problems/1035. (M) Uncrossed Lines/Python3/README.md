## 1035. (M) Uncressed Lines

### `solution.py`

Intuition tells us that we could take a dynamic programming approach, as it seems we could identify a relationship between states. Here, the obvious thing to do is to start examining either the first or last pair of numbers in the two lists. Say we have a recursion fairy (`recurse(i, j)`) that tells us the maximum number of drawable lines given two indices `i` and `j`, where all numbers in `nums1[:i+1]` and `nums2[:j+1]` are considered. At some indices `i` and `j`, there can be two possible outcomes. Either `nums1[i] == nums2[j]`, or `nums1[i] != nums2[j]`. For the former, we can draw a line and ask the recursion fairy for the value considering the remainder of the two lists by calling `recurse(i-1, j-1)`. For the latter, we have to either consider the next number in `nums1`, or consider the next number in `nums2`, whichever is larger. This is simply `max(recurse(i-1, j), recurse(i, j-1))`. Drawing the recursion tree, we also notice that there will be many redundant calls to `recurse()` which we can avoid computing by memoizing values in a 2D list `dp`, where `dp[i][j]` will contain the return value of `recurse(i, j)`.  

The desired answer is the return value of `recurse(len(nums1)-1, len(nums2)-1)`, which we return directly.  

Note that this problem is simply the classic problem of finding the longest common subsequence in disguise.  

#### Conclusion

The time complexity is $O(mn)$ where $n$ is the length if `nums1` and $m$ is the length of `nums2`. `dp` is a $m \times n$ 2D list since there are $mn$ number of possible states that need to be computed. Consequently, the space complexity is also $O(mn)$.  


