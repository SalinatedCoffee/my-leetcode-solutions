## 624. (M) Maximum Distance in Arrays

### `solution.py`
The 2D list `arrays` contains lists of integers that are already sorted in ascending order. We are asked to return the greatest distance between 2 integers in `arrays`, with the distance simply being the absolute difference between the two integers. When selecting the two integers, each integer *cannot* be from the same list in `arrays`.  
Firstly, we know that we only need to deal with the first and last values in each list within `arrays` since it is already sorted. Because we want to maximize the absolute difference between two integers, we would obviously want to use the largest and smallest values(extremes) of each list. Finding the smallest/largest extremes in `arrays` is easy, but there are a few things that we should keep in mind. If the two values are from the same array they cannot form a pair, so we should also keep track of which list the values belong to. When the extremes *are* from the same list, we need to find the next-smallest/largest extremes in `arrays`, which means that we need to keep track of these values as well. Instead of having to mess around with separate variables, we can use a heap for the min/maximum extremes. The heap for the minimum extremes should be a max heap initialized with the largest possible values, since among the current two smallest values and the new value to be added, we want to discard the largest value. We can initialize the heap for the maximums by doing the opposite.  
Iterating over `arrays`, we take the first and last values of each list and push them onto the appropriate heap. The topmost item is then popped off of each of the heaps, before moving onto the next list. Once all lists have been examined we unpack the extremes from the two heaps. If the smallest extreme and largest extreme come from the same list, we compute the difference of the remaining possible pair combinations and return the largest value amongst them.  
  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `arrays`. All lists in `arrays` are examined, and because the two heaps have a fixed maximum size of 3, insert/removal operations take $O(1)$ time to complete. The space complexity is $O(1)$.  
  

