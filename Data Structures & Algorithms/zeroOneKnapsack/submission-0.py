class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [0] * (M + 1)

        for c in range(M + 1):
            if weight[0] <= c:
                cache[c] = profit[0]
        
        for i in range(1, N):
            curr_row = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = cache[c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + cache[c - weight[i]]
                curr_row[c] = max(include, skip)
            cache = curr_row
        
        return cache[M]