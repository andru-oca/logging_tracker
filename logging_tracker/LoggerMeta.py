from typing import Literal


class LoggerMeta(type):

    LevelStr = Literal["critical", "fatal", "error", "warn", "warning", "info", "debug"]
    SeverityStr = Literal[
        "CRITICAL", "FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG", "NOTSET"
    ]

    def __new__(cls, name, bases, dct):

        SEV_DICT: Dict[LevelStr, SeverityStr] = {  # type: ignore
            "debug": "DEBUG",
            "info": "INFO",
            "warning": "WARNING",
            "warn": "WARNING",
            "error": "ERROR",
            "exception": "ERROR",
            "critical": "CRITICAL",
        }

        dct["SEV_DICT"] = SEV_DICT
        # dct["get_logger"] = cls.get_logger

        return super().__new__(cls, name, bases, dct)
