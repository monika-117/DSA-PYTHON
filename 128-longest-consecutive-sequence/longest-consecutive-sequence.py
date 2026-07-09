# nums = [100,4,200,1,3,2]
class Solution:
    def longestConsecutive(self, nums):

        s = set(nums)#{100,4,200,1,3,2}
        longest = 0

        for num in s:

            # Check if it is the start of a sequence
            if num - 1 not in s:

                length = 1

                while num + 1 in s:
                    num += 1
                    length += 1

                longest = max(longest, length)

        return longest