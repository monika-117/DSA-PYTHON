class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)      # Store all numbers in a set
        longest = 0

        for num in s:

            # Check if this is the start of a sequence
            if num - 1 not in s:

                current = num
                count = 1

                # Count consecutive numbers
                while current + 1 in s:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest