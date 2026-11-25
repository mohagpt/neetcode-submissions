class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        INF = float("inf")
        cost = [INF] * n
        cost[src] = 0 
        for _ in range(k+1) : 
            nxt = cost[:]
            for a, b, price in flights : 
                if cost[a] + price < nxt[b] : 
                    nxt[b] = cost[a] + price
            cost = nxt
        return cost[dst] if cost[dst] != INF else -1