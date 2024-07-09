## 1823. (M) Find the Winner of the Circular Game

### `solution.py`
Given the integers `n` and `k`, we are asked to return the number of the winning player among the `n` initial players. With the players arranged in a circle, with the player number increasing by `1` along the clockwise direction(which means that the player number wraps around to `1` by moving clockwise from player `n`) the game starts at player `1`. `k` players are then counted in the clockwise direction(including player `1`), after which the last player to be counted is eliminated from the game. The player next to the removed player(in the clockwise direction) becomes the 'current' player, after which the steps are repeated until there is only one player remaining in the game. The most straightforward method to solve the problem would be to simulate the game, working through the process of eliminating `n-1` players. We can use a queue to store the remaining players as this would allow us to access the current player in $O(1)$ time, as well as rotating the players in linear time. A `deque` is created with the initial players of the game. We then rotate the queue clockwise `k-1` players(since we also include the current player in the count), after which the player to be eliminated will be the first item in the queue. After popping that player from the queue, we rotate the queue yet again, repeating these steps until there is only 1 player remaining.  

#### Conclusion
This solution has a time complexity of $O(nk)$, where $n$ is `n` and $k$ is `k`.   
  


### `solution_2.py`
\<Content\>  

#### Conclusion
\<Content\>  
  

