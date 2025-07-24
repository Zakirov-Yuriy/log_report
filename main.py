# Точка входа в программу

from log_report.cli import parse_args
from log_report.loader import load_logs
from log_report.report_factory import get_report
from tabulate import tabulate


def main():
    args = parse_args()
    logs = load_logs(args.file, args.date)
    report = get_report(args.report, logs).generate()
    print(tabulate(report, headers=["", "handler", "total", "avg_response_time"]))


if __name__ == "__main__":
    main()
