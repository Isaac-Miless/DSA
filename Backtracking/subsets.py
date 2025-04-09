class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums): # null pointer
                res.append(subset.copy())
                return
            
            # include current number in subset
            subset.append(nums[i])
            # process next number (next layer)
            dfs(i + 1)

            # don't include current number
            subset.pop()
            # move on to next layer with the array
            # same as when it came into this call
            dfs(i + 1)
        
        dfs(0)
        return res
