class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create dictionary that will store output data
        output = {}

        for word in strs:
            # Create sorted word for each word
            sorted_word = "".join(sorted(word))
            # Check if sorted word is already in dictionary, then if it's not creates instance with the word, otherwise adds word to existing instance
            if sorted_word not in output.keys():
                output[sorted_word] = [word]
            else:
                output[sorted_word].append(word)
        
        # Returns values of dict
        return output.values()
