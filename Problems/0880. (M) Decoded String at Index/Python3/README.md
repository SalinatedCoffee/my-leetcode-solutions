## 880. (M) Decoded String at Index

### `solution.py`
The first thing to notice is that we should obviously not actually construct the decoded string - given the problem constraints, this string could have a size of roughly 9 *exabytes*. We know that we can easily determine the length of the decoded string by iterating over `s`. If a character is a letter, we add `1` to the tape length. Otherwise, we multiply the tape length by whatever integer the character converts to. Could we use this method to decode up to the last string shorter than `k`, and then return the appropriate character using a modulo operation? While this method is better than decoding the entire string, the improvement is marginal at best since it could be the case that `k` is $2^63$ and the string is $2^62$ long. Thus, we would need to devise an algorithm that eschews the decoding of any string whatsoever.  
Decoding the string going in the forward direction, we would need to at least construct the last string shorter than `k` in order to retrieve the desired character. We have however already established that it is infeasible to do so. By decoding the string in 'reverse', we can reduce the length of the decoded string until we eventually reach the character that would correspond to the `k`th character of the decoded string.   

#### Conclusion
\<Content\>  
  

