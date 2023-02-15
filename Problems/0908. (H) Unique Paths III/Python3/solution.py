class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # try all possible directions
        # back out if square unavailable
        # (already traversed, obstacle, goal but squares remaining)
        # mark traversed squares
        def helper(grid, steps, pos, remaining, ret):
            m, n = pos
            # if OOB, exit
            if not (0 <= m < len(grid) and 0 <= n < len(grid[0])):
                return
            cur_val = grid[m][n]
            # if at obstacle, start, or traversed, exit
            if cur_val == -1 or cur_val == 1 or cur_val == 3:
                return
            # if untraversed, mark current and recurse
            elif cur_val == 0:
                grid[m][n] = 3
                nxt = [(m-1,n), (m,n-1), (m+1,n), (m,n+1)]
                for s in nxt:
                    helper(grid, steps+[pos], s, remaining-1, ret)
                grid[m][n] = 0
            # if end and no squares left add path to ret
            elif cur_val == 2 and not remaining:
                ret.append(steps + [pos])

            return

        # search entire grid for start position and number of untraversed squares
        remaining = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    remaining += 1
                elif grid[i][j] == 1:
                    start = (i, j)          # (row, col)
        i, j = start
        steps = [start]
        ret = []
        nxt = [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]
        for s in nxt:
            helper(grid, steps+[s], s, remaining, ret)
        
        return len(ret)
