class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        
        for i in range(n):
            visited = []
            for j in range(i,n):
                if s[j] in visited:
                    break
                visited.append(s[j])  
            max_len = max(max_len,len(visited))
        return max_len          
        