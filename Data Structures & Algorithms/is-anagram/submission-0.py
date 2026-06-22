class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        
        for i in range(len(s)):
            if s[i] not in s_dict.keys():
                s_dict[s[i]] = 0
            else:
                s_dict[s[i]]  += 1
        
        for i in range(len(t)):
            if t[i] not in t_dict.keys():
                t_dict[t[i]] = 0
            else:
                t_dict[t[i]] += 1
        
        return s_dict == t_dict