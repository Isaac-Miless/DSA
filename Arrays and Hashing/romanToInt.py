class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        n = len(s)
        res = 0
        
        for i in range(n):
            intVer = hashMap[s[i]]
            if i+1 < n and intVer < hashMap[s[i+1]]:
                res -= intVer
            else: res += intVer
                    
        return res
    
    
sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
