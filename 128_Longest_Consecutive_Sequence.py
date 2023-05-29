class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Converts nums to set and creates variable for longest sequence
        nums = set(nums)
        max_len = 0

        for num in nums:
            # Checks if value 1 bigger than num is in set. If not, it means that num is beginning of the set
            if num + 1 not in nums:
                sequence = [num]
                next_value = num - 1
                curr_len = 1
                # As long as theres a value 1 smaller, the vale is appended to the sequence and sequence lenght is added
                while next_value in nums:
                    sequence.append(next_value)
                    next_value -= 1
                    curr_len += 1
                # Check if current sequence is the longest one
                if curr_len > max_len:
                    max_len = curr_len             
                
        return max_len
