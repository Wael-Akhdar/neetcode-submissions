class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []

        len_strs = len(strs)

        if len_strs <= 1:
            res.append(strs)
            return res

        dico = {}

        for i in range(len_strs):
            
            count = [0]*26

            for char in strs[i]:
                count[ord(char) - ord('a')] += 1
            
            sign = tuple(count)
            
            if sign in dico:
                dico[sign].append(strs[i])

            else:
                dico[sign] = [strs[i]]
        

        return list(dico.values())









        