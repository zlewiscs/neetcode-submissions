class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for n1, n2, w in edges:
            adj[n1].append([n2, w])
            adj[n2].append([n1, w])
        
        pq_min = [[0, 0]] # [w, v]
        res = 0
        visit = set()

        while pq_min and len(visit) < n:
            w, v = heapq.heappop(pq_min)
            if v in visit:
                continue

            visit.add(v)
            res += w

            for neighbour, w in adj[v]:
                if neighbour not in visit:
                    heapq.heappush(pq_min, [w, neighbour])
            
        return res if len(visit) == n else -1
