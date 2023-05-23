class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = {}        # Dictionary with number key and repetitions value
        output = []     # List of k numbers
    
        # For each number in input list if the number exists in dictionary add 1 to amout, else create new key-value pair with 1 value
        for num in nums:
            try:
                dic[num] += 1
            except KeyError:
                dic[num] = 1

        # For k times provided
        for i in range(k):
            amount = 0
            num = 0
            # For each key-value checks whats the greatest value
            for key, value in dic.items():
                if value > amount:
                    amount = value
                    num = key
            # Adds number with greatest value to output list and deletes the entry form dict
            output.append(num)
            del dic[num]

        return output
