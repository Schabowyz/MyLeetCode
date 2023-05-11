class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = False
        letter = -1

        for l in range(len(haystack) - len(needle) + 1):
            if haystack[l] == needle[0]:
                for i in range(len(needle)):
                    if haystack[l+i] != needle[i]:
                        match = False
                        break
                    else:
                        match = True
            if match == True:
                letter = l
                break
        
        return letter
