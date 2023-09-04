class RecentCounter:

    def __init__(self):
        self.history = []
        self.pointer = 0
        self.count = 0

    def ping(self, t: int) -> int:
        self.history.append(t)
        self.count += 1
        while self.history[self.pointer] < t - 3000:
            self.pointer += 1
        return self.count - self.pointer
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)