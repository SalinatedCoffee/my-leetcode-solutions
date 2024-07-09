class Solution:
  def findTheWinner(self, n: int, k: int) -> int:
    # simulation on queue
    
    # initialize queue
    players = deque(range(1, n+1))

    # perform simulation
    while len(players) > 1:
      players.rotate(-k)
      players.pop()

    return players.pop()

