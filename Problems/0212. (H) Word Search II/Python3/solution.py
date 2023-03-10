class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # optimized DFS + trie-like dictionaries

    ret = []
    root = {}

    def dfs(r, c, n):
      # recursive DFS
      if board[r][c] == '*':
        return
      c_char = board[r][c]
      # mark letter as visited
      board[r][c] = '*'
      if c_char not in n:
        board[r][c] = c_char
        return
      n = n[c_char]
      # word found, add to ret and prune
      if '#' in n:
        ret.append(n['#'])
        del n['#']
      if r > 0:
        dfs(r-1, c, n)
      if c > 0:
        dfs(r, c-1, n)
      if r < len(board)-1:
        dfs(r+1, c, n)
      if c < len(board[0])-1:
        dfs(r, c+1, n)
      # unmark as visited
      board[r][c] = c_char

    # insert words into trie
    for word in words:
      cur = root
      for c in word:
        cur = cur.setdefault(c, {})
      cur['#'] = word

    for i in range(len(board)):
      for j in range(len(board[0])):
        dfs(i, j, root)
    
    return ret

