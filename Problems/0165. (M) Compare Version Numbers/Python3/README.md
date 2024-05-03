## 165. (M) Compare Version Numbers

### `solution.py`
Converting the version strings to a list of revision integers is fairly straightforward to accomplish through Python's built-in string methods and functions. Comparing the resulting lists are a bit more nuanced, but fortunately not that difficult to implement.  
When both version numbers have the same number of revisions, we simply compare each pair of revisions and immediately return `1` or `-1` depending on which value is larger. If one version is longer than the other, it is larger than the shorter version number *only if* a non-zero value exists in the revision numbers in the longer portion. For example, version `1.0.0.0` is considered equal to `1.0` since the longer portion `0.0` does not contain a non-zero revision number. On the other hand, `1.0.0.1` *is* larger than `1.0` since the remaining substring `0.1` contains `1`, a non-zero value. With this in mind, we can start implementing a solution.  
We first compare revisions from each version number until we run out of values to compare from one version number. If at any point the values are not equal, we can immediately return `1` or `-1` accordingly. If the comparisions are completed without returning, we check for any remaining revision numbers. `0` can be returned if there are none, as this would mean that the two version numbers are identical. Otherwise, we select the longer version number and scan the remaining revisions. Again, if a value is non-zero, we immediately return `1` or `-1` depending on which version number is currently selected. If all of the revisions are zero, the iteration exits normally and we return `0`.  

#### Conclusion
This solution has a time complexity of $O(m+n)$ where $m$ and $n$ are the lengths of `version1` and `version2`, respectively. Splitting the version numbers into revisions, and converting the revisions into integers take linear time that scales with the length of the version string. Comparing revision numbers is also a linear time operation, as there can be at most $\max(m, n) / 2 + 1$ pairs to examine. The space complexity is also $O(m+n)$, as the converted list of revision numbers are kept in memory.  
  

