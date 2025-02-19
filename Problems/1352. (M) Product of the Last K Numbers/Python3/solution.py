class ProductOfNumbers:
  # prefix products

  def __init__(self):
    self._prods = [1]

  def add(self, num: int) -> None:
    if num == 0:
      self._prods = [1]
    else:
      self._prods.append(self._prods[-1] * num)

  def getProduct(self, k: int) -> int:
    if k > len(self._prods) - 1:
      return 0
    return self._prods[-1] // self._prods[-k-1]

