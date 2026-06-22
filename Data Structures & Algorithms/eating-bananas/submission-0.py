class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        l = 1
        r = max(piles)
        k = max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            curr_hour = self.hours_taken(piles, mid)
            
            if curr_hour <= h:
                k = min(mid, k)
                r = mid - 1
            else:
                l = mid + 1
        
        return k
    
    def hours_taken(self, piles, trial):
        res = 0
        for pile in piles:
            res += math.ceil(pile / trial)
        
        return res