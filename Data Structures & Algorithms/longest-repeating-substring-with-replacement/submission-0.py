class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict()
        max_freq = 0
        l = 0
        res = 0

        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            max_freq = max(max_freq, cnt[s[r]])

            while r - l + 1 - max_freq > k:
                cnt[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res