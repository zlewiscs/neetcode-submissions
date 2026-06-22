class Solution {
    public int countPaths(int[][] grid) {
        return dfs(grid, 0, 0, new HashSet());
    }

    private int dfs(int[][] grid, int r, int c, Set<String> visited) {
        if (r < 0 || c < 0 || r >= grid.length || 
            c >= grid[0].length || grid[r][c] == 1 ||
            visited.contains(r + "," + c)
        ) {
            return 0;
        }

        if (r == grid.length - 1 && c == grid[0].length - 1) {
            return 1;
        }

        visited.add(r + "," + c);

        int count = dfs(grid, r + 1, c, visited) + 
                    dfs(grid, r - 1, c, visited) +
                    dfs(grid, r, c + 1, visited) +
                    dfs(grid, r, c - 1, visited);
        
        visited.remove(r + "," + c);

        return count;
    }
}
