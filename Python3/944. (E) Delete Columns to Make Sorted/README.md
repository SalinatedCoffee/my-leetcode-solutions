## 944. (E) Delete Columns to Make Sorted

### `solution.py`
The obvious way to go about this problem is to simply walk the columns while comparing two adjacent letters. One thing to note is that lists with one row is *always* valid, which is explicitly checked before doing anything else. Then we transpose the given 2D list and iterate over row-first using nested loops. Whenever we find that the current letter is lexicographically 'smaller'(quite literally so in both ASCII and UNICODE) than the previous one, we increment a counter and break from the inner loop.

#### Conclusion
This solution runs in $O(mn)$ time, where $m$ is the length of the columns and $n$ is the length of the rows. Since the transpose creates a new list, the space complexity is $O(mn)$ as well. You might be thinking - "*Well, if we just use the given array instead of transposing wouldn't we have the same time complexity but use constand space?*", and you would be absolutely right! I thought I was being clever but what really happened was that I over-thought the solution which in turn made me look like an idiot.
Still, I've left this solution in as a example of what not to do.

### `solution_2.py`
Same approach as `solution.py`, but using the given list instead of creating a new one.

#### Conclusion
As previously discussed, the solution runs in $O(mn)$ time and uses $O(1)$ space.
There are other 'clever' solutions by other people that involves sorting, but remember that Python's `sorted()` internally uses Timsort which has a time complexity of $O(n \log n)$. One-liner solutions are *very* cool; but this is Leetcode, not code golf.
