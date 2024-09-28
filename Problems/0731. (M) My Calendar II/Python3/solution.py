class MyCalendarTwo:
  # brute force

  def __init__(self):
    self.events = []
    self.overlap = []

  def _overlaps(self, s1: int, e1: int, s2: int, e2: int) -> bool:
    # return False if [s1, e1) does not overlap with [s2, e2)
    # return True otherwise
    return max(s1, s2) < min(e1, e2)

  def _getOverlap(self, s1: int, e1: int, s2: int, e2: int) -> (int, int):
    # return overlapping section of intervals [s1, e1) and [s2, e2)
    return (max(s1, s2), min(e1, e2))

  def book(self, start: int, end: int) -> bool:
    # check for triple booking
    for s, e in self.overlap:
      if self._overlaps(s, e, start, end):
        return False
    for s, e in self.events:
      if self._overlaps(s, e, start, end):
        self.overlap.append(self._getOverlap(s, e, start, end))
    self.events.append((start, end))
    
    return True

