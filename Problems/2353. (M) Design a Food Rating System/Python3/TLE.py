class FoodRatings:
  # sort every time highestRated is called
  
  def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    n = len(foods)
    self._food = dict(zip(foods, ratings))
    self._cuis = defaultdict(list)
    for f, c in zip(foods, cuisines):
      self._cuis[c].append(f)

  def changeRating(self, food: str, newRating: int) -> None:
    self._food[food] = newRating

  def highestRated(self, cuisine: str) -> str:
    c_sorted = sorted(self._cuis[cuisine], reverse=True)
    c_sorted.sort(key=lambda x: self._food[x])
    return c_sorted[-1]

