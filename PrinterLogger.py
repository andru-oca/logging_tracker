from typing import Callable
from .LoggerMeta import LoggerMeta


class PrinterLogger(metaclass=LoggerMeta):
    """Mock logger, que hace un print e ignora el severity completamente"""

    log_levels = ["debug", "info", "warning", "warn", "error", "exception", "critical"]

    def __init__(self) -> None:
        self._set_attr_log_levels()

    @staticmethod
    def _log_func(msg, *args, **kwargs):
        print(msg)

    def _set_attr_log_levels(self) -> None:
        for level in self.log_levels:
            setattr(self, level, self._log_func)

    def log(self, msg, level: str, *args, **kwargs):
        assert level in self.SEV_DICT
        func: Callable = getattr(self, level)
        func(msg, *args, **kwargs)
