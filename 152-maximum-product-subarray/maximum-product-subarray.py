class Solution:
    def maxProduct(self, nums):

        maxProd = nums[0]
        minProd = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):

            current = nums[i]

            # Store old values
            oldMax = maxProd
            oldMin = minProd

            # Find new maximum product
            maxProd = max(current,
                          current * oldMax,
                          current * oldMin)

            # Find new minimum product
            minProd = min(current,
                          current * oldMax,
                          current * oldMin)

            # Update answer
            answer = max(answer, maxProd)

        return answer