class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = []
        
        for op in operations:
            if op not in ["C","D","+"]:
                res.append(int(op))
            elif op == "C":
                res.pop()
            elif op == "D":
                res.append(res[-1]*2)
            elif op == "+":
                res.append(res[-1]+res[-2])
        
        return sum(res)
