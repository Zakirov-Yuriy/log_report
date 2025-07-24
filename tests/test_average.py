# Тест проверяет базовую логику расчёта среднего времени отклика

import pytest
from log_report.reports.average import AverageReport

def test_average_report():
    logs = [
        {"url": "/test", "response_time": 0.1},
        {"url": "/test", "response_time": 0.3},
        {"url": "/other", "response_time": 0.2},
    ]
    report = AverageReport(logs).generate()
    assert report[0][1] == "/test"
    assert report[0][2] == 2
    assert abs(report[0][3] - 0.2) < 1e-6
