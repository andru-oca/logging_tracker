import logging
from typing import Callable, Optional


from .LoggerMeta import LoggerMeta


class FileLogger(metaclass=LoggerMeta):
    """Logger almacena en un file"""

    FORMAT = "%(asctime)s [%(levelname)s]: %(message)s"
    log_levels = ["debug", "info", "warning", "error", "exception", "critical"]

    def __init__(
        self,
        filename: str,
        level: str,
        format: Optional[str] = None,
    ) -> None:

        self.filename = filename
        self.level = level
        self.format = format
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.SEV_DICT[self.level])

        formatter = logging.Formatter(format if format else self.FORMAT)

        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(self.SEV_DICT[self.level])
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self._set_level_attr()

    def _set_level_attr(self) -> None:
        for level in self.log_levels:
            setattr(self, level, getattr(self.logger, level))

    def log(self, msg, level: str, *args, **kwargs):

        assert level in self.SEV_DICT
        func: Callable = getattr(self.logger, level)
        func(msg, *args, **kwargs)
