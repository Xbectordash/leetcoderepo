class Solution:
    def matchexp(self,openexp,closeexp):
        if openexp=="(" and closeexp==")" or openexp=="[" and closeexp=="]" or openexp=="{" and closeexp=="}":
            return True
        else: return False    
    def isValid(self, s: str) -> bool:
        stack = []    
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack or not self.matchexp(stack[-1],i):
                    return False
                stack.pop()
        return len(stack) == 0            
                         



        