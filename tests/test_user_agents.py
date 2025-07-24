# Проверяем, что отчёт UserAgentsReport корректно подсчитывает и сортирует user-agent


import pytest
from log_report.reports.user_agents import UserAgentsReport


def test_user_agents_report():
    logs = [
        {"http_user_agent": "Chrome"},
        {"http_user_agent": "Chrome"},
        {"http_user_agent": "Firefox"},
        {"http_user_agent": "Safari"},
        {"http_user_agent": "Safari"},
        {"http_user_agent": "Safari"},
    ]
    report = UserAgentsReport(logs).generate()

    assert report[0][1] == "Safari"
    assert report[0][2] == 3
    assert report[1][1] == "Chrome"
    assert report[2][1] == "Firefox"
