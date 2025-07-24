# Тест проверяет, что функция load_logs корректно фильтрует логи по дате

from log_report.loader import load_logs
import tempfile

def test_log_filter_by_date():
    log_lines = [
        '{"@timestamp": "2025-06-22T10:00:00+00:00", "url": "/ok", "response_time": 0.1}',
        '{"@timestamp": "2025-06-23T10:00:00+00:00", "url": "/skip", "response_time": 0.2}'
    ]

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.writelines(line + "\n" for line in log_lines)
        tmp.flush()
        logs_filtered = load_logs([tmp.name], date_filter="2025-06-22")

    assert len(logs_filtered) == 1
    assert logs_filtered[0]["url"] == "/ok"
