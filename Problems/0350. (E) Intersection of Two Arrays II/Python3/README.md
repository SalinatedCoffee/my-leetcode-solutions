## 350. (E) Intersection of Two Arrays II

### `solution.py`
Given two lists of integers we are asked to return an array that corresponds to the intersection of the two lists, where the elements do not have to be unique. The brute force solution would involve iterating over one array for every element in the other array, which would be very time consuming. We can instead store the frequencies of each unique value within each list in a dictionary, which will allow us to verify whether an element exists in the other list in constant time.  
Two `Counter`s are first initialized, one with `nums1` and the other with `nums2`. We then iterate over the key value pairs of `nums1`(or `nums2`) while checking each key against the other dictionary. If the key exists, we take the lesser of the two values and append the key by that number. Because we want a list of values that appear in both lists, it is sufficient to iterate over only one array.  

#### Conclusion
The time complexity is $O(m+n)$, where $m$ and $n$ are the length of `nums1` and `nums2`, respectively. Counting the number of unique values in each array takes $O(m)$ and $O(n)$ time, and iterating over the key value pairs of `nums1` takes $O(m)$ time. Thus, the overall time complexity is $O(m+n+m) = O(m+n)$. The space complexity is also $O(m+n)$, due to the dictionaries `n1_freq` and `n2_freq`.  
  

