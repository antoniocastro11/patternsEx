from collections import defaultdict

class ProxyMetrics:
    def __init__(self):
        self.counters = defaultdict(int)
        self.counters["success"] = 0
        self.counters["error"] = 0

    def notify(self, event: str):
        self.counters[event] += 1

    def get_metrics(self):
        return dict(self.counters)

metrics = ProxyMetrics()
