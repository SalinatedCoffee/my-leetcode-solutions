## 2038. (M) Remove Colored Pieces if Both Neighbors are the Same Color

### `solution.py`
The problem being about players taking turns and labeled medium may tempt you to think about a dynamic programming solution, but the reality is that this problem is much simpler than it first seems.  
A player can only remove a pieces when its neighbors also have the same color as that piece. That is, any moves made by a player will *never* affect the possible moves of the other player. Thus, in order to determine which player will win a game, we only need the number of moves that can be made by each player. Because Alice (player `A`) always goes first, Alice wins if she can make more moves than Bob. The number of available moves for each player can be trivially counted by iterating through `colors`. `colors` can be 'split' into substrings that only consist of `A`s or `B`s. For each substring `t`, a player can make `len(t) - 2` moves given the rules described in the problem. As such, we can iterate along `colors` while counting the number of possible moves that can be made by Alice and Bob. Then we simply compare the number of moves and return `True` or `False` accordingly.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `colors`. `colors` is iterated over exactly once, while each iteration only involves a handful of operations that each take $O(1)$ time. The space complexity is $O(1)$.  
  

