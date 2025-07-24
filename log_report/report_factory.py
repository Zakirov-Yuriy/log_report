# Выбор и возврат нужного отчётного класса по имени фабрика

from .reports.average import AverageReport
from .reports.user_agents import UserAgentsReport

REPORTS = {
    "average": AverageReport,
    "user_agents": UserAgentsReport,
}


def get_report(name: str, logs: list[dict]):
    if name not in REPORTS:
        raise ValueError(f"Unknown report type: {name}")
    return REPORTS[name](logs)
