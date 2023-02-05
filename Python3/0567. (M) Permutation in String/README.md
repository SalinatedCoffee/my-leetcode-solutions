## 567. (M) Permutation in String

### `solution.py`
The first thing to identify is what a *permutation* actually is. A permutation of a string should have the same length and include exactly the same number of letters as the original string. This gives a clue as to how to determine whether a substring of `s2` is a permutation of `s1`. Since brute forcing all possible permutations is obviously not optimal, we can instead count the number of letters in `s1` and compare that to the letter count of a substring of `s2` with length `len(s1)`.  
We initialize two lists of length 26 that stores the letter counts of `s1` and `s2[0:len(s1)]`. Then we enter a loop where we first check whether the letter counts match (indicating that a substring of `s2` is a permutation of `s1`) and if not, advance the substring forward by 1. Note that whenever we move the substring window, we can simply decrement the count for the letter at index `i` and increment at index `j` instead of recounting all letters in `s2[i:j]`. Once we exit the loop we check for a count match one more time since the while loop checks for a match *before* advancing the window.  
The solution also does a sanity check before doing anything since `s2` cannot possibly be a permutation of `s1` if it is shorter.  
  
#### Conclusion
The time complexity is $O(n+26m)$ where $n$ is the length of `s1` and $m$ is `len(s2) - len(s1)`. We iterate over `s1` once to generate the letter count, and over `s2[len(s1):]` once to look at substrings of length `len(s1)`. During every iteration step we check for a letter count match which performs 26 operations over `cnt1` and `cnt2`.  
For space complexity, this solution uses $O(1)$ space since the lists storing the letter counts scales with the size of the alphabet instead of the length of `s1` or `s2`.  
  
