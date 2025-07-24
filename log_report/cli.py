# Обработка аргументов командной строки с помощью argparse

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Log report generator")
    parser.add_argument("--file", nargs="+", required=True, help="Path(s) to log files")
    parser.add_argument("--report", required=True, choices=["average", "user_agents"], help="Report type")
    parser.add_argument("--date", help="Filter logs by date (YYYY-MM-DD)")
    return parser.parse_args()
