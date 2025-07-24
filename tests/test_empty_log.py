# Тесты для пустых логов

from log_report.reports.average import AverageReport
from log_report.reports.user_agents import UserAgentsReport

# Проверяем, что отчёт AverageReport корректно обрабатывает пустой список лого

def test_average_empty_log():
    logs = []
    report = AverageReport(logs).generate()
    assert report == []

# Проверяем, что отчёт UserAgentsReport корректно обрабатывает пустой список логов

def test_user_agents_empty_log():
    logs = []
    report = UserAgentsReport(logs).generate()
    assert report == []
