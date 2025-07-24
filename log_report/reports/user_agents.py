# Реализацию отчёта по User Agent

from collections import Counter
from .base import BaseReport

class UserAgentsReport(BaseReport):
    def generate(self):
        counter = Counter()
        for entry in self.logs:
            ua = entry.get("http_user_agent", "unknown")
            counter[ua] += 1

        result = []
        for i, (agent, count) in enumerate(counter.most_common()):
            result.append([i, agent, count])
        return result


