class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s)-1

        while i < j:
            
            if not s[i].isalnum():
                i += 1
            
            if not s[j].isalnum():
                j -= 1

            if s[i].capitalize() != s[j].capitalize():
                print(f"s[i]:{s[i]} s[j]:{s[j]} i:{i} j:{j}")
                return False
            
            i += 1
            j -= 1
        
        return True