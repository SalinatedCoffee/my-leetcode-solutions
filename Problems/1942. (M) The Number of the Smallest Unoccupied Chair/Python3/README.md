## 1942. (M) The Number of the Smallest Unoccupied Chair

### `solution.py`
There are an infinite number of chairs in a room, which are incrementally labeled with an integer starting from `0`. `n` people are attending an event in that room, and are also labeled with a unique integer in the range `[0, n)`. When a person arrives, they immediately occupy a vacent chair with the smallest label. When they leave they immediately vacate the chair that they were sitting on, which means that if a person leaves and another arrives at the same time, the arriving person will end up occupying the chair that the leaving person had just vacated. Given these conditions and the list of arrival/departure times `times` where `times[i]` represents the arrival/departure times for the `i`-th person, we are asked to return the label of the chair that the `targetFriend`-th person will end up sitting in.   
Because we want to assign vacant seats in ascending order of their labels, and want to reintroduce newly vacent seats back into the pool of available seats, intuition tells us that we can use heaps to solve this problem. We can use two heaps; one will store the currently available seats, and the other will store the occupied ones. As we want to access the available seats in ascending order of their labels, the label of each seat should be used as the comparison key. For the 'occupied' heap we want to be able to 'recycle' seats in order of the time that they are no longer occupied, and so the end time of the person in the seat should be used as the comparison key. While processing each person in order of their arrival, we first look at the 'occupied' heap and remove any seats that are currently vacent, adding them back into the 'vacent' heap. We can now assign a seat to the current person by popping a vacent seat from the 'vacent' heap. If the person is `targetFriend`, we immediately return the label of the seat that was about to be assigned.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `times`. `times` is sorted in ascending order of the arrival time of each person, which takes $O(n\log n)$ time to perform using Python's built in sort. `times` is then iterated over, with the heaps `vacent` and `occupied` potentially being interacted with for each element. A seat is removed from and added to a heap every time its vacency changes. Because there are only $n$ people, a vacency change can occur at most $O(2n) = O(n)$ times over the entire duration of the event. Thus, we can say that the entirety of the searching step will require $O(n\log n)$ time to complete since `vacent` and `occupied` can hold at most $O(n)$ elements, making each insert/removal operation cost $O(\log n)$ time. The space complexity is $O(n)$, due to the sorting step and the two heaps.  
  
