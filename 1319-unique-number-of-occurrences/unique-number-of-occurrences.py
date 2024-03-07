class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
           dic[i] = dic.get(i,0)+1
        if len(dic.values()) == len(set(dic.values())):
            return True
        else: return False    

         