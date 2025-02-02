class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, vals = 0, self.data.get(key, [])
        l, r = 0, len(vals)-1
        
        while l <= r:
            m = (l+r)//2
            if vals[m][1] <= timestamp:
                res = vals[m][0]
                l = m+1
            else:
                r = m-1

        return res
