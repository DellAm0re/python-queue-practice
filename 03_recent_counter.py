from collections import deque


class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)


if __name__ == "__main__":
    counter = RecentCounter()
    for t in [1, 100, 3001, 3002]:
        print(counter.ping(t))  # 1, 2, 3, 3
