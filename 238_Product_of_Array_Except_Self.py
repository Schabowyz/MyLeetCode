class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Output list
        output = []

        # Appends all the prefix values for each number in the table
        pre = 1
        for i in range(len(nums)):
            output.append(pre)
            pre = pre * nums[i]
        
        # Modifies all the values in output table with postifx value
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * post
            post = post * nums[i]
        
        return output
