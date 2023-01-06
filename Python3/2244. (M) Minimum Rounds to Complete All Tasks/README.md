## 2244. (M) Minimum Rounds to Complete All Tasks

### `solution.py`
The word that instinctively comes to mind upon encountering the word 'minimum' (at least for me) is recursion. But no, that's a trap. This problem can easily be solved by simple iteration. The key is realizing that given round 'sizes' of 2 or 3, *all* sets of tasks have a valid solution as long as they don't have a single task with a certain difficulty. First we pack all tasks into a dictionary for easy manipulation, after which we first check whether the given task list has a valid solution. Then we iterate over all difficulties within the dictionary.  
For each difficulty, we determine if it can be completed in 1 round (2 or 3 remaining tasks), 2 rounds (4, 5, or 6 remaining tasks), or more. If we can exhaust the remaining tasks at the current difficulty in 1 or 2 rounds, we update the number of rounds accordingly and move on to the next difficulty. Else we do 3 tasks, update the number of rounds, and then check the remaining tasks again.  
  
#### Conclusion
Constructing the dictionary, `t_d.keys()`, and `t_d.values()` all takes $O(n)$ time. The `while` loop runs in $O(n/2)$ time, so overall this solution has a time complexity of $O(n). Memory-wise, the solution uses $O(2n) = O(n)$ space since a task list (of size $n$) comprised of tasks with unique difficulty levels will result in a dictionary of size $n$.  


### `solution_2.py`
This is just a touched-up version of the first solution, where instead of explicitly using a list of the dictionary's keys we iterate over the dictionary directly which removes the need of accessing the keys by index (eliminating the call to `t_d.keys()`). The validity check is also folded inside the loop since iterating over `list(t_d.values())` is redundant if we're iterating over `t_d` anyways.
#### Conclusion
Theoretically this solution has the same time and space complexity compared to the previous one, but practically it uses a lot less memory thanks to the removal of calls to `t_d.keys()` and `t_d.values()`. A good example of where asymptotic running time isn't everything, and obvious optimizations should be made whenever possible.  


### `solution_3.py`
So we've improved the memory usage, but can we make this solution run any faster(according to the submission statistics, obviously yes)? Can't we just... *divide* by 3 instead of subtracting multiple times?  
Indeed, just throw a modulo and a few integer divisions in there and we're done!   

#### Conclusion
The solution again has the same running time and memory usage as the first two, but in practice runs a lot faster since it saves a lot of iterations on 'normal' task lists where a certain difficulty level has a *reasonable* number of tasks. Floating point division certainly uses more CPU cycles compared to simple subtraction, but in this case the difference is negligible and you (probably) shouldn't be bothering with this level of micro-optimization if you're writing code in Python.  
