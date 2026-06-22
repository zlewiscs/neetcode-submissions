class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            return 1 if s[0] == s[1] else 2

        mp = defaultdict()
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)

        return res
        