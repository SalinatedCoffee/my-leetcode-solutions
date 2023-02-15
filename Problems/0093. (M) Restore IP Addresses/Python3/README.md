## 93. (M) Restore IP Addresses

### `solution.py`
This is a classic backtracking problem. First, we need to identify the conditions for exiting early. A substring is invalid when the first digit is 0 but has a length longer than 1, or when it is larger than 255. Now we may iterate through the string recursively, backtracking whenever the current substring is invalid and adding the generated IP address to a return list when the end of the string is reached and 4 numbers have been validated.  

#### Conclusion
This runs in $O(1)$ time and space since there are at most $3^3$ valid IP addresses than can be generated from a given string.  
One thing to note that this problem can be easily brute-forced since the search space is limited to a sufficiently small size. We may also implement an iterative version of this solution with 3 nested loops since we know the recursion depth at which correct answers will be found.  

