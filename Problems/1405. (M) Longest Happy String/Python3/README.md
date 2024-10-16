## 1405. (M) Longest Happy String

### `solution.py`
Starting with the empty string, we can insert the characters `'a'`, `'b'`, or `'c'` to form a string. The string cannot contain more than 2 consecutive identical characters. If we are allowed to insert *at most* `a`, `b`, and `c` occurrences of `'a'`, `'b'`, and `'c'`, respectively, we are asked to return the longest possible string that can be constructed. To maximize the length of the generated string, we should obviously try to insert the most available character as much as possible. Because this character will change depending on how many of which character has already been inserted into the string, we can use a max heap to keep track of the characters to greedily add the most available character and incrementally build up the string. At each insertion we pop the top-most item off the stack and examine the previous two characters. If they are identical to the character from the stack, we pop another element off of the stack and insert it instead. The two characters are then pushed back onto the stack with updated counts. If the stack is empty, we break out of the loop since the string cannot be inserted into any further.  

#### Conclusion
This solution has a time complexity of $O(a+b+c)$, where $a$, $b$, and $c$ are `a`, `b`, and `c`, respectively. The while loop repeats until the heap is empty, and since a character is discarded only when its counter hits zero the loop will repeat $O(a+b+c)$ times in the worst case. Operations on `heap` are considered as requiring $O(1)$ time as the size of `heap` is bounded at `3`. The space complexity is $O(1)$, excluding the intermediate list of characters that is concatenated to generate the returned string.  
  

