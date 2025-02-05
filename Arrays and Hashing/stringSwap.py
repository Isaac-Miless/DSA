class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2: return True
        if len(s1) != len(s2): return False
        
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        
        if len(diff) != 2:
            return False
        
        # print(s1[diff[0]], s2[diff[1]])
        # print(s1[diff[1]], s2[diff[0]])
        
        # check the characters are equal at the differing indices (could be swapped)
        return s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]

sol = Solution()
print(sol.areAlmostEqual("bank", "kanb")) # True
print(sol.areAlmostEqual("attack", "defend")) # False
