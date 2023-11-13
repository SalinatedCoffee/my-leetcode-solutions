## 2785. (M) Sort Vowels in a String

### `solution.py`
The idea is simple - we extract only the vowels from `s`, sort them in ascending order by ASCII code, and then overwrite the vowels in `s` with the sorted list. Iterating over `s`, we check whether a character is a vowel. If it is, we append the character to the list `v_list`. After the entirety of `s` has been examined, we sort `v_list` by ASCII codes. We then proceed to constructing the return string by once again iterating over `s`. If a character is a vowel, we take a vowel from `v_list`. Once the list of characters is fully populated we simply concatenate its contents by using `.join()`.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `s`. We sort the vowels in `s`, the number of which is obviously bound by $n$. The space complexity is $O(n)$, both because of `s_list` and the sorting step.  
  

