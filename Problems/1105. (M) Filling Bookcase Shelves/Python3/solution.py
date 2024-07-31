class Solution:
  def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
    # top-down dynamic programming (memoization)
    
    n = len(books)
    # height of tallest book in current shelf
    self.h = 0

    @cache
    # return minimum height sum when placing books[idx:] books
    # and current shelf has w empty space remaining
    def recurse(idx, w):
      # base case
      if idx == n:
        return self.h
      
      # try placing book in new shelf
      h_t = self.h
      self.h = books[idx][1]
      ret = h_t + recurse(idx+1, shelfWidth-books[idx][0])
      self.h = h_t
      # try placing book in current shelf
      if books[idx][0] <= w:
        self.h = max(self.h, books[idx][1])
        ret = min(ret, recurse(idx+1, w-books[idx][0]))
      
      return ret

    return recurse(0, shelfWidth)

