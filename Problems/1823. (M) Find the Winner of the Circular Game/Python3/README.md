## 1823. (M) Find the Winner of the Circular Game

### `solution.py`
Given the integers `n` and `k`, we are asked to return the number of the winning player among the `n` initial players. With the players arranged in a circle, with the player number increasing by `1` along the clockwise direction(which means that the player number wraps around to `1` by moving clockwise from player `n`) the game starts at player `1`. `k` players are then counted in the clockwise direction(including player `1`), after which the last player to be counted is eliminated from the game. The player next to the removed player(in the clockwise direction) becomes the 'current' player, after which the steps are repeated until there is only one player remaining in the game. The most straightforward method to solve the problem would be to simulate the game, working through the process of eliminating `n-1` players. We can use a queue to store the remaining players as this would allow us to access the current player in $O(1)$ time, as well as rotating the players in linear time. A `deque` is created with the initial players of the game. We then rotate the queue clockwise `k-1` players(since we also include the current player in the count), after which the player to be eliminated will be the first item in the queue. After popping that player from the queue, we rotate the queue yet again, repeating these steps until there is only 1 player remaining.  

#### Conclusion
This solution has a time complexity of $O(nk)$, where $n$ is `n` and $k$ is `k`.   
  


### `solution_2.py`
The problem can also be modeled using a recurrence relation - as a matter of fact, this problem is a well known topic in computer science and mathematics called the [Josephus problem](https://en.wikipedia.org/wiki/Josephus_problem#The_general_case). Essentially, eliminating a player from a pool of `n` people reduces the player count to `n-1`. And because the next round starts at the player next to the one that was just eliminated, it is a subproblem of the previous round, allowing us to establish a recurrence relation between the state transitions. Let the function $f(p, s)$ return the index of the last remaining player among $p$ total players skipping $s$ people. When $p = 1$, $f$ should obviously return $0$. Otherwise we know that the value of subproblem $f(p-1, s)$ will return the index of the winning player, but **in the context of the subproblem**. To shift this index back into the context of the current problem, we need to add $s$ to the index and modulo that value by $p$. We add $s$ because the subproblem shifts the index by $-s$ by skipping $s$ people, and modulo the index by $p$ because the players are arranged in a circle that wraps around. By definition, the value we want is the return value of $f(\texttt{n}, \texttt{k})$, which we can directly return.  

#### Conclusion
The solution has a time complexity of $O(n)$. `recurse` is called `n` times, and since each call takes $O(1)$ time to complete the overall time complexity comes out to be $O(n)$. The space complexity is also $O(n)$, due to the recursion stack.  
We are asked to implement a $O(n)$ time and $O(1)$ space solution in the follow-up, which can be done so by implementing an interative version of this solution. Because `recurse(n, k)` depends on the value of `recurse(n-1, k)`, we can easily implement a bottom-up dynamic programming solution that starts with a player count of `1` and works its way up to `n`.  
  

