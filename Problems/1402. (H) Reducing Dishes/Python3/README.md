## 1402. (H) Reducing Dishes

### `solution.py`
We obviously want to discard the dishes with the smallest satisfaction values as they will contribute the least to the like-time coefficient. Getting to these satisfaction values however is not straightforward, so we sort `satisfaction` to gain access to the `n`th smallest value in constant time.  
Now we know that we are only interested in the suffixes of `satisfaction`, as we established earlier. The problem now becomes determining which dish maximizes the like-time coefficient. The brute force approach where we try all suffixes starting at index 0 is obviously not optimal, as redundant accesses occur on the dishes to the right side. Instead, we can consider suffixes that 'start' from the end of `satisfaction`. Then the suffix sum is trivial to compute, and the like-time coefficient also becomes easy to compute since it is simply `suffix_sum[i] + lt_coeff[i+1]` for a suffix that starts at index `i`. This is because of how the like-time coefficient is defined; For a list of dishes, the l-t coefficient is the sum of the dishes multiplied by their indices. Since we are extending the suffix towards the left, the positions of the dishes do not change and the multiplication is 'amortized' by adding the suffix sum to the previous coefficient.  
We may exit early once the suffix sum becomes negative, as any suffixes past that point will only decrease the like-time coefficient.  
  
#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `satisfaction`. The sorting step takes $O(n\log n)$ time, and the coefficient computations takes $O(n)$ time. The space complexity is $O(n)$ since Python's `.sort()` uses Timsort, which has a worst case space complexity of $O(n)$.  
  

