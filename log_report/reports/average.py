# Реализация отчёта average среднее время отклика по URL

from collections import defaultdict
from .base import BaseReport

class AverageReport(BaseReport):
    def generate(self):
        stats = defaultdict(lambda: {"count": 0, "total_time": 0.0})
        for log in self.logs:
            url = log.get("url")
            time = log.get("response_time", 0)
            if url:
                stats[url]["count"] += 1
                stats[url]["total_time"] += time

        result = []
        for i, (url, data) in enumerate(
            sorted(stats.items(), key=lambda x: -x[1]["count"])
        ):
            avg = data["total_time"] / data["count"]
            result.append([i, url, data["count"], round(avg, 3)])
        return result


