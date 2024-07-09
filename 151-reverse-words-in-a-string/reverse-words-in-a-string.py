
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.rstrip()
        s = s.split(' ')
        s = s[::-1]
        ans = ""
        for i in s:
            ans += i
            ans += " "
        ans =" ".join(ans.split())     
        return ans.rstrip()