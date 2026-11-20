
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            len_w = len(word)
            res += str(len_w) + "#"
            res += word
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0

        while i < len(s):

            l = i
            nb = ""

            while s[l].isdigit():
                nb += s[l]
                l += 1

            len_nb = len(nb)
            nb = int(nb)

            k = ""

            for j in range (i + len_nb+1, nb + i + len_nb+1):
                k += s[j]

            res.append(k)
            
            i += nb + len_nb + 1 
        
        print(res)
        return res

             

            
