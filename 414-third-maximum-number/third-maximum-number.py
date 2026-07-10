class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))   # Remove duplicates

        nums.sort()              # Sort in ascending order

        if len(nums) < 3:
            return nums[-1]      # Return largest element

        return nums[-3]          # Return third largest