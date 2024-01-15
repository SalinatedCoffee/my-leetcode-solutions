## 2225. (M) Find Players With Zero or One Losses

### `solution.py`
As we are only interested in the number of losses for each player, we can simply count the losses and use that to determine whether a player needs to be added to the return list. The losses can be trivially counted using a dictionary, where the key would be the player number and the value the losses that the player has. Iterating over `matches`, we increment the value of `losses[l]` by `1` where `losses` is the dictionary previously mentioned and `l` is the `1`st item of the current 2-element list in `matches`. One thing to keep in mind is that we are asked to return the list of players that have played at least once. This can be tracked in the same dictionary by simply creating a new key-value pair in `losses` for the winning player if it doesn't already exist. Once every match has been examined, we sort the keys of `losses` (players) in ascending order, and add each player to the appropriate list in `ret`.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `matches`. Counting losses takes $O(n)$ time, but we sort the keys in `losses` to examine players in ascending order, and this takes $O(n)$ times since `losses` can at most contain $2n$ unique players. Determining whether to add a player to a list takes $O(n)$ time. The space complexity is $O(n)$ as `losses` and the key sorting step both uses $O(n)$ memory.  
  

