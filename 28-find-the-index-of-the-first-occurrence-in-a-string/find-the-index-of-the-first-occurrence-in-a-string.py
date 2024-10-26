class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if needle is empty
        if needle == "":
            return 0
        # Check if needle exists in haystack
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        