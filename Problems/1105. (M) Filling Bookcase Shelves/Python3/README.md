## 1105. (M) Filling Bookcase Shelves

### `solution.py`
The list `books` contains information about books to be placed in a bookshelf, where `books[i][0]` is the width and `books[i][1]` is the height of book `i`. When `shelfWidth` is the width of the bookshelf, we are asked to determine and return the minimum sum of the height of all shelves after every book has been placed. The books can also only be placed in order of their appearance in `books`; book `i` must be placed after placing book `i-1`, book `i-1` must be placed after book `i-2`, and so on.  
At first glance it may seem that the problem can be solved through a greedy algorithm based approach that tries to fit as many books onto a single shelf. When trying a few small examples however, we quickly realize that this is not the case. For example, let `books = [[1, 1], [1, 3], [1, 2]]` and `shelfWidth = 2`. The aforementioned greedy algorithm would put the `0`th and `1`st book in the first shelf and the `2`nd book in the second shelf, yielding the total height of `max(1, 3) + 2 = 5`. However, if we place only the `0`th book on the first shelf and the remaining books on the second shelf, we would have gotten the total height of `1 + max(3, 2) = 4`, which is less than the previous value of `5`. Now that we have convinced ourselves that a greedy approach would fail, the next angle of attack would be to try and implement a dynamic programming based solution. What would a state in the recurrence relation represent, and what parameters would be required to represent a unique state? Representing a state with only the index of the current book that needs to be placed would not be enough, since the decision of placing the current book(and any following books) depend on the remaining space in the current shelf. Thus, we need to introduce another parameter that represents the horizontal space remaining in the current shelf.  
The function `recurse(idx, w)` will return the minimum sum of shelf heights when placing books in `books[idx:]` where the remaining space in the current shelf is `w`. A global variable `self.h` will keep track of the tallest book in the current shelf. When `recurse` is first called and `idx == len(books)`, all books have been placed in the bookshelf and so we immediately return the height of the tallest book in the current shelf which is `self.h`. Otherwise, we first try placing the book in a new shelf and try placing it in the current shelf. We keep a copy of `self.h` in the variable `h_t` before we do so, as we will have to revert this value to its original state before the second recursive call. Placing a book in a new shelf means that we need to add the tallest height of the current shelf to the minimum height sum of placing the remaining books. By placing the `idx`-th book in a new shelf, the shelf will now have the remaining space of `shelfWidth - books[idx][0]` and maximum height of `books[idx][1]`. We save the intermediate value of `h_t + recurse(idx+1, shelfWidth - books[idx][0])` after assigning `books[idx][1]` to `self.h`. `self.h` is then reverted back to its previous value before attempting to place book `idx` in the current shelf. If there is enough space, placing the book would result in the remaining space of `w - books[idx][0]` and the new maximum height of `max(self.h, books[idx][1])`. We compare the value from the previous choice with that of `recurse(idx+1, w - books[idx][0])` and return the smaller of the two.  
By definition of `recurse` we want the return value of `recurse(0, 0)`, which we can return directly.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ is `shelfWidth` and $n$ is the length of `books`. Each state in the recurrence relation is represented by two integers, with one bound by $m$ and the other by $n$. Evaluating the value of a state takes $O(1)$ time and all possible states are examined, resulting in the overall time complexity of $O(mn)$. The space complexity is also $O(mn)$ since the value of all states are kept in memory over the lifetime of the algorithm.  
  