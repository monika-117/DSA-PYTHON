class Solution:
    def findDuplicate(self, nums):
        # Step 1: Start both pointers
        slow = nums[0]
        fast = nums[0]

        # Step 2: Find the meeting point
        while True:
            slow = nums[slow]          # Move 1 step
            fast = nums[nums[fast]]    # Move 2 steps

            if slow == fast:
                break

        # Step 3: Reset slow
        slow = nums[0]

        # Step 4: Find the duplicate
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow