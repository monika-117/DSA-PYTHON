class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):

            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if -asteroids[i] > stack[-1]:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroids[i]:
                    stack.pop()
                    break   
                elif stack[-1] > -asteroids[i]:
                    break        
            else:
                stack.append(asteroids[i])
        return stack
            