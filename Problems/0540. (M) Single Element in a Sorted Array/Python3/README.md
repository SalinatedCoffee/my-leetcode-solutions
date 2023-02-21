## 540. (M) Single Element in a Sorted Array

### `solution.py`
Implementing a linear solution is trivial, so of course the problem asks us to come up with a logarithmic solution. Seeing the word 'logarithmic' in this context we immediately reach for binary search. However we are not given a target to search for and thus we need to figure out some other criteria of choosing between the left and right halves. This is where things get slightly wonky as the problem doesn't *explicitly mention* that elements always appear in pairs (except for the unique value, obviously) but implies that they do in the two examples given. So taking this assumption as the truth then we can see that if we ensure that the left half always contains an even number of elements, we can compare the last element in the left hand side and the first element in the right hand side. If they are equal that would mean that there is a unique element somewhere in the left half that has 'pushed' pairs out of alignment, and vice versa.  
For this solution, I have implemented the iterative flavor of binary search but the recursive version would work here also.  
  
#### Conclusion
This solution has a time complexity of $O(\log n)$ where $n$ is the length of `nums`, per the problem specification. The space complexity is $O(1)$ as the iterative version of binary search uses a fixed amount of extra memory.  
  

