class Router:
  # double ended queue with dictionaries and sets
  def __init__(self, memoryLimit: int):
    self._cap = memoryLimit
    self._memory = deque()
    # maps destination to list of corresponding packets in insertion order
    self._dest_packet_list = defaultdict(list)
    self._packets = set()

  def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
    if (source, destination, timestamp) in self._packets:
      return False
    if len(self._memory) == self._cap:
      self.forwardPacket()
    self._packets.add((source, destination, timestamp))
    self._memory.append((source, destination, timestamp))
    self._dest_packet_list[destination].append(timestamp)
    return True

  def forwardPacket(self) -> List[int]:
    if len(self._memory) == 0:
      return []
    res = self._memory.popleft()
    if self._dest_packet_list[res[1]]:
      self._dest_packet_list[res[1]].pop(0)
    self._packets.remove(res)
    return list(res)

  def getCount(self, destination: int, startTime: int, endTime: int) -> int:
    if destination not in self._dest_packet_list:
      return 0
    packets = self._dest_packet_list[destination]
    i = bisect_left(packets, startTime)
    j = bisect_right(packets, endTime)
    return j - i

