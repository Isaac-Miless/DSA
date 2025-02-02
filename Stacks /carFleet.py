class Solution:
    def carFleet(self, target, position, speed):
        # Optimal (Stack): O(n logn) // Space: O(n)
        pairs = [[p,s] for p,s in zip(position,speed)]
        pairs.sort(reverse=True) # sorted(pairs)[::-1]
        stack = []
        
        for p,s in pairs:
            stack.append(float(target-p) / s) # time = distance / speed
            print(stack)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # collision, treat them as one fleet
        return len(stack)

sol = Solution()
position = [6,8]
speed = [3,2]
target = 10

print(sol.carFleet(target, position, speed))
