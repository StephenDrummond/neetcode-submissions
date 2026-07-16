from bisect import bisect
class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hm:
            self.hm[key].append((timestamp, value))
        else:
            self.hm[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""

        idx = bisect(self.hm[key], timestamp, key=lambda x:x[0])

        return self.hm[key][idx - 1][1] if idx != 0 else ""
