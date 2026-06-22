class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s) or len(t) == 0:
            return ""

        t_counter = Counter(t)
        window = defaultdict()
        
        have = 0
        need = len(t_counter)
        res = [-1, -1]
        res_size = float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in t_counter and window[c] == t_counter[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_size:
                    res = [l, r]
                    res_size = r - l + 1
                
                window[s[l]] -= 1

                if s[l] in t_counter and window[s[l]] < t_counter[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res

        return s[l : r + 1] if res_size != float("infinity") else ""



        

