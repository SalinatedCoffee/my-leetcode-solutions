## 874. (M) Walking Robot Simulation

### `solution.py`
A robot initially sits on the origin of an infinite 2D grid, pointed north. Some points on the grid have obstacles on them, and the robot should stop just short of the obstacle if it ever encounters one and then move to its next instruction. A single instruction can have a value of `-2`, `-1`, or any integer in the range `[1, 9]`. The instructions `-2` and `-1` turns the robot 90 degrees to the left and right, respectively, and positive integers make the robot move forward that number of times. For example, if the instructions are `[-1, 3]` and there is an obstacle at `(0, 2)`, the robot will first turn to the right to face east and then attempt to move 3 times forward. As it does so it will encounter an obstacle after moving once, and the robot's final position will be `(0, 1)`. Given the list of instructions `commands` and obstacles `obstacles`, we are asked to return the largest squared Euclidean distance between the robot and the origin while carrying out the instructions.  
We can easily simulate the problem by using a few loops and conditionals. The direction the robot is facing can be represented by a list of unit vectors which can be used to compute the new position of a robot whenever it carries out a move instruction. Turning the robot can be done by in/decrementing the index of the current unit vector by `1` and applying modulo 4 to the new value. When a robot receives a move command, we incrementally move forward by `1` until it either moves the required distance or encounters an obstacle in front of it. In either case, we compute the squared Euclidean distance from the robot to the origin and update the largest distance as necessary.  
  

#### Conclusion
This solution has a time complexity of $O(m+n)$, where $m$ is the length of `obstacles` and $n$ the length of `commands`. Generating a set from `obstacles` requires $O(m)$ time to complete, and simulating each instruction in `commands` takes $O(n)$ time since one instruction can be simulated in $O(1)$ time. The space complexity is $O(m)$, due to the set `obs_set`.  
  

