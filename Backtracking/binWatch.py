class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        def backtrack(turnedOn, start, hour, minute):
            if turnedOn == 0:
                if hour < 12 and minute < 60:
                    res.append(str(hour) + ":" + str(minute).zfill(2))
                return
            for i in range(start, 10):
                if i < 4:
                    backtrack(turnedOn - 1, i + 1, hour + (1 << i), minute)
                else:
                    backtrack(turnedOn - 1, i + 1, hour, minute + (1 << (i - 4)))
        res = []
        backtrack(turnedOn, 0, 0, 0)
        return res
