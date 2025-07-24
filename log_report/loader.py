# Чтение логов из файла и фильтрация по дате

import json


def load_logs(files, date_filter=None):
    logs = []
    for file in files:
        with open(file, encoding="utf-8") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    if date_filter:
                        if not entry["@timestamp"].startswith(date_filter):
                            continue
                    logs.append(entry)
                except json.JSONDecodeError:
                    continue
    return logs
