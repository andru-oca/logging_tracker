from typing import Callable, Optional, Dict, TYPE_CHECKING
from .LoggerMeta import LoggerMeta

if TYPE_CHECKING:
    from google.cloud.logging import Logger


class WrapperLogger:
    """Wrapper para el logger de GCP para que sea mas intuitivo su uso"""

    LevelStr = Literal["critical", "fatal", "error", "warn", "warning", "info", "debug"]
    SeverityStr = Literal[
        "CRITICAL", "FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG", "NOTSET"
    ]

    SEV_DICT: Dict[LevelStr, SeverityStr] = {
        "debug": "DEBUG",
        "info": "INFO",
        "warning": "WARNING",
        "warn": "WARNING",
        "error": "ERROR",
        "exception": "ERROR",
        "critical": "CRITICAL",
    }


    log_levels = ["debug", "info", "warning", "warn", "error", "exception", "critical"]

    def __init__(self, logger: "Logger") -> None:
        self._logger = logger
        self._labels: Optional[Dict[str, str]] = None
        self._set_attr_log_levels()

    @property
    def labels(self) -> Optional[Dict[str, str]]:
        return self._labels

    @labels.setter
    def labels(self, new_labels: Dict[str, str]) -> None:
        assert new_labels is not None
        assert isinstance(new_labels, dict)
        assert all(
            isinstance(k, str) and isinstance(v, str) for k, v in new_labels.items()
        )
        self._labels = new_labels

    def _set_attr_log_levels(self) -> None:
        for level in self.log_levels:
            setattr(self, level, self._get_log_func(level))

    def _get_log_func(self, level: str) -> Callable:

        def log_func(text) -> None:
            labels = self.labels
            if labels is None:
                self._logger.log_text(
                    text if isinstance(text, str) else str(text),
                    severity=self.SEV_DICT[level],  # SeverityStr
                )
            else:
                self._logger.log_text(
                    text if isinstance(text, str) else str(text),
                    severity=self.SEV_DICT[level],  # SeverityStr
                    labels=labels,
                )

        return log_func

    def log(self, msg, level: str):
        assert level in self.SEV_DICT
        func: Callable = getattr(self, level)
        func(msg)
