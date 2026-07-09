class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        # Step 2: Find the element just larger than nums[i] and swap
        if i >= 0:
            for j in range(n - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

        # Step 3: Reverse the elements after index i
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(nums, i + 1, n - 1)