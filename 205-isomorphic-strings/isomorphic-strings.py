class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Two dictionaries to store the mapping from s to t and t to s
        s_to_t = {}
        t_to_s = {}

        # Loop through each character pair
        for char_s, char_t in zip(s, t):
            # Check if there is an existing mapping from s to t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            # Check if there is an existing mapping from t to s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True
        