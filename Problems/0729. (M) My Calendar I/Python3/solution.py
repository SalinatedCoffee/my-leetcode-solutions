# binary search

# use external module
# https://grantjenks.com/docs/sortedcontainers/sortedlist.html
from sortedcontainers import SortedList

class MyCalendar:
  def __init__(self):
    self.events = SortedList()

  def book(self, start: int, end: int) -> bool:
    idx = self.events.bisect_right((start, end))
    if (idx > 0 and self.events[idx-1][1] > start) or \
      (idx < len(self.events) and self.calendar[idx][0] < end):
      return False
    self.events.add((start, end))

    return True

