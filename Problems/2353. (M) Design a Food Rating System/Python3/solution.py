class FoodRatings:
  # priority queues using heaps

  def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    n = len(foods)
    # value of self._food[f] is (r, c) where r and c are rating and cuisine
    # of food f
    self._food = dict(zip(foods, zip(ratings, cuisines)))
    # value of self._cuis[c] is max heap of tuples (r, f) where r is rating of food f
    self._cuis = defaultdict(list)
    for f, c in zip(foods, cuisines):
      heappush(self._cuis[c], (-self._food[f][0], f))

  def changeRating(self, food: str, newRating: int) -> None:
    c = self._food[food][1]
    self._food[food] = (newRating, c)
    heappush(self._cuis[c], (-newRating, food))

  def highestRated(self, cuisine: str) -> str:
    r, f = self._cuis[cuisine][0]
    while -r != self._food[f][0]:
      heappop(self._cuis[cuisine])
      r, f = self._cuis[cuisine][0]

    return f

