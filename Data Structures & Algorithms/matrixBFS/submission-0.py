class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        path_length = 0

        queue.append((0, 0))
        visit.add((0, 0))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return path_length
                
                nexts = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in nexts:
                    if r + dr < 0 or c + dc < 0 or \
                    r + dr == ROWS or c + dc == COLS or \
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1:
                        continue
                    
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
                
            path_length += 1
            
        return -1