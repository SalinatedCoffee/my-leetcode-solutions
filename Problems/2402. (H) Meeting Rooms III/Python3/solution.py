class Solution:
  def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
    # greedy algorithm on heaps

    m = len(meetings)
    meetings.sort()
    # vacant is min heap of available rooms
    # booked is min heap of booked meetings and their rooms, using end time as key
    vacant, booked = [i for i in range(n)], []
    heapify(vacant)
    usage = [0]*n

    for begin, end in meetings:
      # process meetings that have ended before current
      while booked and booked[0][0] <= begin:
        _, room = heappop(booked)
        heappush(vacant, room)
      # if rooms are available, book one
      if vacant:
        room = heappop(vacant)
        usage[room] += 1
        heappush(booked, (end, room))
      # if all rooms booked, 'schedule' current meeting to earliest available
      else:
        e, room = booked[0]
        usage[room] += 1
        heappush(booked, (e+end-begin, room))
        heappop(booked)
  
    # find earliest most used room
    tgt = max(usage)
    for i in range(n):
      if usage[i] == tgt:
        return i

    # this line should never run
    return -1

