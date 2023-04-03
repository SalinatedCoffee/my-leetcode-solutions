class Solution:
  def numRescueBoats(self, people: List[int], limit: int) -> int:
    # sort, then two pointers

    people.sort()
    lo, hi = 0, len(people)-1
    ret = 0
    while lo <= hi:
      # if two people cannot fit, always optimal to ship heaviest person
      if people[lo]+people[hi] <= limit:
        lo += 1
      hi -= 1
      ret += 1

    return ret

