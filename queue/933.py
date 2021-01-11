import collections

class RecentCounter:
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while len(self.q) != 0 and t - self.q.[0] > 3000:
            self.q.popleft()
        return len(self.q)

   
