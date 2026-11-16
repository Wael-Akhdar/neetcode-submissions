class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        len_s = len(s)

        if len_s != len(t):
            return False

        hash_map = {}

        for i in range (len_s):

            char_s = s[i]
            char_t = t[i]

            hash_map[s[i]] = 1 + hash_map.get(s[i],0)
            hash_map[t[i]] = hash_map.get(t[i],0) - 1

        for val in hash_map.values():
            if val != 0:
                return False
        
        return True


