class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for s, d, w in edges:
            adj_list[s].append([d, w])

        shortest_path = {}
        pq_min = [[0, src]]

        while pq_min:
            w1, n1 = heapq.heappop(pq_min)
            if n1 in shortest_path:
                continue
            
            shortest_path[n1] = w1

            for n2, w2 in adj_list[n1]:
                if n2 not in shortest_path:
                    heapq.heappush(pq_min, [w1 + w2, n2])
                
        for i in range(n):
            if i not in shortest_path:
                shortest_path[i] = -1
        
        return shortest_path