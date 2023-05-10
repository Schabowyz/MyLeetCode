class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        # Except error if program runs out of letters in word
        try:
            # For i in range of 1st word coz prefix can't be longer than any word
            for i in range(len(strs[0])):
                # Checks word with 1st word, if letter doesnt match breaks the loop with false match
                for word in strs:
                    if word[i] != strs[0][i]:
                        match = False
                        break
                    else:
                        match = True
                # If match is true, adds letter to prefix and goes to next letter, otherwise breaks the loop
                if match == True:
                    prefix += strs[0][i]
                else:
                    break
        except IndexError:
            pass
        return prefix
