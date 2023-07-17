## 1125. (H) Smallest Sufficient Team

### `solution.py`

The size constraints on the inputs, namely `1 <= len(req_skills) <= 16` and `1 <= len(people) <= 60`, gives us a hint as to how we should be approaching this problem. First of all, we can represent a set of skills as a bitstring, where the `i`th bit being set to `1` means that the set includes the skill `req_skills[i]`. We may also use the same method to represent a set of team members, given the constraint on `people` (other languages will have to use larger data types, such as `long` in Java). One main advantage of using this method is that the set difference can be trivially computed using a handful of bit operations.  

Returning to the actual computation step, we want to find the smallest team that possesses all skills described in `req_skills`. Assuming there is some team with some set of skills, and some person `i`, we can determine whether the person `i` could have belonged in that team by taking the set of skills that `i` does not possess, and comparing it against the team's skill set. If the intersection of these two sets is **not** equal to the team's skill set, it means that the person `i` possesses skills that could have contributed to the team, and thus we try adding that person to a team that possesses the skill set equal to the intersection we just computed. However if the newly formed team has more members that a different team (`team` has more set bits than `dp[i]`, which can be conveniently computed with the aid of built-in method `int.bit_count()`) with an identical skill set, we simply ignore the new team and move on to a different one.  

Once `dp` has been populated (where `dp[i]` is the bitmask representation of individuals that form the smallest team with skill set expressed as bitmask `i`), the value we want will be stored in `dp[-1]`, which we convert back to a list of indices of team members in `people`.  

#### Conclusion

This solution has a time complexity of $O(2^mn)$ where $m$ is the length of `req_skills` and $n$ is the length of `people`. We iterate over all possibile subsets of `req_skills`, of which there are $2^m$ of. For each iteration we iterate over the entierety of `people`, which takes $O(n)$ time. The space complexity is $O(2^m)$.  

Note that if we had tried to compute over all possible selections of people, this solution would have timed out as the bound on the size of `people` is much larger than that of `req_skills`.  

In essence, this is exactly the optimization version of the [Minimum set cover problem]([Set cover problem - Wikipedia](https://en.wikipedia.org/wiki/Set_cover_problem)), which happens to be NP-hard.  


