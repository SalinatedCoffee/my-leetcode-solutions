## 2141. (H) Maximum Running Time of N Computers

### `solution.py`
One thing to note is that we can let a computer drain a battery until it is empty. Batteries can be swapped in zero time, and as such we can keep a computer on past its battery's remaining charge if we switch to a fresh one *just* as the current one goes flat. This lets us effectively treat a pool of multiple batteries as one giant battery, which makes things easier for us.  
Let's first think about the trivial case where there are just enough batteries to go around (or `n == len(batteries)`). In this case the answer is simply `min(batteries)`, since there are no extra batteries to swap in whenever a battery is fully discharged. Then what about the case where we have one extra battery? Now, when the smallest battery is depleted we can swap over to the extra battery to extend the running time. If we have enough to extend it up to the second-smallest battery's amount, the running time would now be the charge level of the second-smallest battery. If we also have some charge left over, we can extend the running time even still, but now we need to expend 2 minutes of charge for 1 minute of running time since we are charging two batteries now instead of one. This can be generalized if we sort `batteries` in ascending order. After setting aside the last `n` batteries to be initially used (we'll call this subarray `live`) and keeping track of the sum of charges of the extra batteries in `extra`, we can say that in order to extend the running time (which is currently `live[0]`) up to `live[1]`, we need to expend `live[1] - live[0]` from `extra`. If we want to extend it even further, up to `live[2]`, we would need to expend `2 * (live[2] - live[1])` and so on. After extending the running time to `live[i]`, if we still have some charge left over in `extra` we can distribute the remaining charge by adding `floor(extra // (i+1))` to the running time.  
One more thing - we cannot reallocate the leftover charge from batteries in `live[i+1:]`, since those batteries are already in use in their respective computers.  

#### Conclusion
This solution has a time complexity of $O(m\log m)$, where $m$ is the length of `batteries`. We sort `batteries` to obtain `batt_sorted`, which takes $O(m\log m)$ in Python. The space complexity is $O(m)$, since Python's built-in sort uses $O(m)$ space during runtime.  


### `solution_2.py`
Based on the principles described above, we can take a different approach where we use binary search on possible running times. Since we have established that for some running time `t` we cannot utilize the remaining charge in batteries larger than `t`, we can verify whether `t` is an attainable running time by taking the sum of `batteries` where a charge larger than `t` is 'truncated' down to `t`. If this sum is larger than `t * n`, it means it is indeed possible to power `n` computers for `t` minutes.  
The initial search space is `1` to `sum(batteries) // n`. Since a battery has at least `1` minute of charge, and it is guaranteed that there are at least `n` batteries available, the minimum possible running time is `1`. The maximum possible time is `sum(batteries) // n` because this represents the ideal situation where there is just enough extra charge to run all computers up to `live[-1]`.  

#### Conclusion
The time complexity is $O(m\log k)$, where $k$ is `max(batteries)`. The initial search space is $[1, mk/n]$, thus binary search will iterate $O(\log mk/n)$ times. Each iteration takes $O(m)$ time to run as the verification step involves iterating over `batteries`, hence the overall running time of $O(m\log k)$ when $k \gg m$ and $k \gg n$. The space complexity is $O(1)$.  
  

