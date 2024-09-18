from typing import Callable, Optional, Dict, TYPE_CHECKING, Union, Any
from .LoggerMeta import LoggerMeta

if TYPE_CHECKING:
    from google.cloud.logging import Logger


class WrapperLogger:
    """Wrapper around GCP logger for more intuitive usage."""

    log_levels = ["debug", "info", "warning", "warn", "error", "exception", "critical"]

    def __init__(self, logger: "Logger") -> None:
        """Initialize WrapperLogger with a Google Cloud Logger instance."""
        self.SEV_DICT = {
            "debug": "DEBUG",
            "info": "INFO",
            "warning": "WARNING",
            "warn": "WARNING",
            "error": "ERROR",
            "exception": "ERROR",
            "critical": "CRITICAL",
        }
        print(f"Initialized SEV_DICT: {self.SEV_DICT}")

        self._logger = logger
        self._labels: Optional[Dict[str, str]] = None
        self._set_attr_log_levels()

    @property
    def labels(self) -> Optional[Dict[str, str]]:
        """Optional labels for logging messages."""
        return self._labels

    @labels.setter
    def labels(self, new_labels: Dict[str, str]) -> None:
        """Set labels for the logger, ensuring they are a dict of strings."""
        if not isinstance(new_labels, dict):
            raise ValueError("Labels must be a dictionary.")
        if not all(isinstance(k, str) and isinstance(v, str) for k, v in new_labels.items()):
            raise ValueError("All keys and values in labels must be strings.")
        self._labels = new_labels

    def _set_attr_log_levels(self) -> None:
        """Dynamically set logging level methods."""
        for level in self.log_levels:
            setattr(self, level, self._get_log_func(level))

    def _get_log_func(self, level: str) -> Callable[[Union[str, Any]], None]:
        """Return the appropriate logging function for the specified level."""

        def log_func(text: Union[str, Any]) -> None:
            """Log the message with the specified severity and labels."""
            if not isinstance(text, str):
                text = str(text)  # Ensure the log message is always a string
            
            labels = self.labels
            if labels is None:
                self._logger.log_text(text, severity=self.SEV_DICT[level])
            else:
                self._logger.log_text(text, severity=self.SEV_DICT[level], labels=labels)

        return log_func

    def log(self, msg: Union[str, Any], level: str) -> None:
        """Log a message at the specified log level."""
        if level not in self.SEV_DICT:
            raise ValueError(f"Invalid log level: {level}")
        
        func: Callable = getattr(self, level)
        func(msg)
