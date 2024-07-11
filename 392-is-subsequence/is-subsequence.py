class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "" and not t == "":
            return True  
        if s == "" and t == "":
            return True 
        if not s == "" and t == "":
            return False        

        l = 0
        r = len(s)-1

        for i in t:
            if s[l] == i:
                l += 1
                if l == len(s):
                    return True
        return False            
        