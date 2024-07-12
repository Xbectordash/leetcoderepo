class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to count characters in magazine
        magazine_count = {}
        
        # Count each character in magazine
        for char in magazine:
            if char in magazine_count:
                magazine_count[char] += 1
            else:
                magazine_count[char] = 1
        
        # Check if ransomNote can be constructed from magazine
        for char in ransomNote:
            if char in magazine_count and magazine_count[char] > 0:
                magazine_count[char] -= 1
            else:
                return False
        
        return True                 
        