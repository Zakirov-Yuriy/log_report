# Базовый интерфейс отчёта

from abc import ABC, abstractmethod


class BaseReport(ABC):
    def __init__(self, logs: list[dict]):
        self.logs = logs

    @abstractmethod
    def generate(self):
        pass

